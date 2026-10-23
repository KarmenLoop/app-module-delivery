#!/usr/bin/env python3
# Copyright 2026 KarmenLoop. License: See LICENSE.
"""Run registered application acceptance checks and retain real evidence."""
import hashlib,json,os,subprocess,sys,time,uuid
from pathlib import Path
from host_support import Database,Problem,need,identifier,content,stamp,atomic,under,file_record,schema,string,integer,array,main

REQ=schema({'id':string(80),'title':string(200),'check_id':string(80)},['id','title','check_id'])
TOOLS=[
 {'name':'app_init','description':'Create a project acceptance plan using the workspace owner\'s pre-registered check file.','inputSchema':schema({'project_id':string(80),'goal':string(2000),'requirements':array(REQ)},['project_id','goal','requirements'])},
 {'name':'app_status','description':'Read the plan and check actual evidence hashes before reporting acceptance.','inputSchema':schema({'project_id':string(80)},['project_id']),'annotations':{'readOnlyHint':True}},
 {'name':'app_run_check','description':'Run one exact registered argv command, retaining actual exit, logs and artifact hashes.','inputSchema':schema({'project_id':string(80),'check_id':string(80),'expected_revision':integer()},['project_id','check_id','expected_revision'])},
 {'name':'app_export','description':'Save the current plan and checked results as a local JSON handoff.','inputSchema':schema({'project_id':string(80)},['project_id'])}]

def configuration(workspace):
 p=under(workspace,'.app-delivery-checks.json');need(p.is_file(),'CHECKS_MISSING','Create .app-delivery-checks.json with the exact authorized commands first.')
 need(p.stat().st_size<=100000,'CHECKS_TOO_LARGE','Check configuration exceeds 100 KB.')
 raw=p.read_bytes();value=json.loads(raw);need(isinstance(value,dict) and 0<len(value)<=100,'INVALID_CHECKS','Register 1-100 checks.')
 for key,entry in value.items():
  identifier(key);need(isinstance(entry,dict),'INVALID_CHECKS','Each check must be an object.');argv=entry.get('argv')
  need(isinstance(argv,list) and 0<len(argv)<=40 and all(isinstance(a,str) and 0<len(a)<=4000 for a in argv),'INVALID_CHECKS','Each check requires an exact argv array.')
  need(type(entry.get('timeout_seconds',30)) is int and 1<=entry.get('timeout_seconds',30)<=60,'INVALID_CHECKS','Timeout must be 1-60 seconds.')
  need(type(entry.get('expected_exit',0))is int,'INVALID_CHECKS','Expected exit must be an integer.')
  under(workspace,entry.get('cwd','.'));need(isinstance(entry.get('artifacts',[]),list) and len(entry.get('artifacts',[]))<=30,'INVALID_CHECKS','Too many artifact paths.')
  need(isinstance(entry.get('inputs',[]),list) and len(entry.get('inputs',[]))<=30,'INVALID_CHECKS','Too many input paths.')
  for path in entry.get('artifacts',[])+entry.get('inputs',[]):under(workspace,path)
 return value,hashlib.sha256(raw).hexdigest()

def status(db,key,workspace):
 p=db.get(key);need(p,'PROJECT_MISSING','Initialize this project first.');_,digest=configuration(workspace);p=json.loads(json.dumps(p));p['configuration_current']=digest==p['configuration_sha256']
 for result in p['results'].values():
  if result['status']=='PASS':
   try:
    actual=[file_record(workspace,x['path']) for x in result['artifacts']];inputs=[file_record(workspace,x['path']) for x in result.get('inputs',[])];result['evidence_current']=actual==result['artifacts'] and inputs==result.get('inputs',[])
   except Problem:result['evidence_current']=False
   if not result['evidence_current'] or not p['configuration_current']:result['status']='STALE'
 p['accepted']=bool(p['requirements']) and all(p['results'].get(x['check_id'],{}).get('status')=='PASS' for x in p['requirements']) and p['configuration_current'] and not p.get('running')
 return p

def reconcile(db,key):
 p=db.get(key)
 if not p or not p.get('running'):return
 active=p['running'];path=db.root/'runs'/active['id']/'receipt.json'
 if not path.is_file():return
 result=json.loads(path.read_text())
 need(result['run_id']==active['id'] and result['check_id']==active['check_id'] and result['configuration_sha256']==p['configuration_sha256'],'RECEIPT_MISMATCH','The saved result does not match the active check.')
 def finish():
  current=db.get(key)
  if current.get('running')!=active:return
  current['running']=None;current['revision']+=1;current['results'][result['check_id']]=result;current['history'].append(result);db.put(key,current);db.event('check.finished',{'project':current['project_id'],'run':active['id'],'status':result['status']})
 db.transaction(finish)

def dispatch(name,a,args):
 db=Database(args.root);workspace=Path(args.workspace).resolve();key='project:'+identifier(a['project_id'])
 try:
  reconcile(db,key)
  if name=='app_init':
   checks,digest=configuration(workspace);need(len(a['requirements'])>0,'REQUIREMENTS_REQUIRED','At least one requirement is needed.')
   ids=[identifier(x['id']) for x in a['requirements']];need(len(ids)==len(set(ids)),'DUPLICATE_REQUIREMENT','Requirement IDs must be unique.')
   for r in a['requirements']:need(r['check_id'] in checks,'UNKNOWN_CHECK','Every requirement must reference a registered check.')
   def init():
    need(db.get(key)is None,'PROJECT_EXISTS','Existing project was preserved.');p={'project_id':a['project_id'],'goal':content(a['goal']),'requirements':a['requirements'],'revision':1,'configuration_sha256':digest,'results':{},'history':[],'running':None};db.put(key,p);db.event('project.created',{'id':a['project_id']});return p
   return db.transaction(init)
  if name=='app_status':return status(db,key,workspace)
  if name=='app_export':
   p=status(db,key,workspace);path=db.root/(identifier(a['project_id'])+'-acceptance.json');atomic(path,json.dumps(p,indent=2)+'\n');return {'path':str(path),'accepted':p['accepted'],'revision':p['revision']}
  checks,digest=configuration(workspace);check_id=identifier(a['check_id']);need(check_id in checks,'UNKNOWN_CHECK','This check is not registered.')
  run_id=uuid.uuid4().hex
  def begin():
   p=db.get(key);need(p,'PROJECT_MISSING','Initialize first.');need(p['revision']==a['expected_revision'],'STALE_REVISION','Read the latest plan before running a check.');need(not p.get('running'),'CHECK_RUNNING','Another check is still running. Inspect its process before recovery.');need(p['configuration_sha256']==digest,'CONFIGURATION_CHANGED','The registered commands changed. Create a newly reviewed plan.');p['running']={'id':run_id,'check_id':check_id};p['revision']+=1;db.put(key,p)
  db.transaction(begin);check=checks[check_id];run_dir=db.root/'runs'/run_id;run_dir.mkdir(parents=True,mode=0o700)
  request={'run_id':run_id,'check_id':check_id,'configuration_sha256':digest,'workspace':str(workspace),'check':check}
  atomic(run_dir/'request.json',json.dumps(request)+'\n')
  try:
   runner=subprocess.Popen([sys.executable,str(Path(__file__).with_name('runner.py')),str(run_dir/'request.json')],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,start_new_session=os.name=='posix',creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name=='nt' else 0)
  except OSError:
   # No child was started; clear this exact reservation and preserve the failed attempt.
   def undo():
    p=db.get(key);p['running']=None;p['revision']+=1;db.put(key,p)
   db.transaction(undo);raise
  runner.wait(timeout=check.get('timeout_seconds',30)+15)
  need((run_dir/'receipt.json').is_file(),'RESULT_UNKNOWN','The check has no terminal receipt. Inspect the saved run; it was not retried.')
  reconcile(db,key);result=json.loads((run_dir/'receipt.json').read_text())
  return {'result':result,'project':status(db,key,workspace)}

 finally:db.close()

if __name__=='__main__':raise SystemExit(main('app_module_delivery','1.1.0',TOOLS,dispatch))
