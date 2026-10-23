#!/usr/bin/env python3
# Copyright 2026 KarmenLoop. License: See LICENSE.
"""Own one registered check independently of the host connection."""
import json,os,signal,subprocess,sys,time
from pathlib import Path
from host_support import atomic,stamp,under,file_record,Problem

def stop(p):
 if p.poll() is not None:return
 if os.name=='posix':os.killpg(p.pid,signal.SIGKILL)
 else:subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],capture_output=True,timeout=10)
 p.wait(timeout=10)

def run(path):
 request=json.loads(path.read_text());check=request['check'];workspace=Path(request['workspace']);folder=path.parent;process=None
 result={k:request[k] for k in ['run_id','check_id','configuration_sha256']};result.update(status='FAIL',started_at=stamp(),exit_code=None,argv=check['argv'],cwd=str(under(workspace,check.get('cwd','.'))),expected_exit=check.get('expected_exit',0),artifacts=[],detail=None,stdout=str(folder/'stdout.txt'),stderr=str(folder/'stderr.txt'))
 try:
  result['inputs']=[file_record(workspace,p) for p in check.get('inputs',[])]
  with (folder/'stdout.txt').open('wb') as out,(folder/'stderr.txt').open('wb') as err:
   process=subprocess.Popen(check['argv'],cwd=result['cwd'],stdin=subprocess.DEVNULL,stdout=out,stderr=err,start_new_session=os.name=='posix',creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name=='nt' else 0)
   deadline=time.monotonic()+check.get('timeout_seconds',30)
   while process.poll() is None:
    if time.monotonic()>deadline:result['detail']='TIMEOUT';stop(process);break
    if any((folder/n).stat().st_size>8*1024*1024 for n in ['stdout.txt','stderr.txt']):result['detail']='LOG_LIMIT_EXCEEDED';stop(process);break
    time.sleep(.05)
   result['exit_code']=process.returncode
  result['artifacts']=[file_record(workspace,p) for p in check.get('artifacts',[])]
  if result['exit_code']==result['expected_exit'] and not result['detail']:result['status']='PASS'
  if [file_record(workspace,p) for p in check.get('inputs',[])]!=result['inputs']:result['status']='INCONCLUSIVE';result['detail']='INPUT_CHANGED_DURING_RUN'
 except (OSError,Problem) as error:result['detail']=str(error)
 finally:
  if process is not None and process.poll() is None:stop(process)
  result['finished_at']=stamp();atomic(folder/'receipt.json',json.dumps(result,indent=2)+'\n')
 return 0
if __name__=='__main__':raise SystemExit(run(Path(sys.argv[1])))
