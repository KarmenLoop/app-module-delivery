import json,subprocess,sys,tempfile,unittest,time,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/app-module-delivery/scripts/host.py'
class HostTest(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.base=Path(self.tmp.name);self.workspace=self.base/'workspace';self.workspace.mkdir();self.data=self.base/'private'
 def tearDown(self):self.tmp.cleanup()
 def argv(self,host='codex',subject=None):return [sys.executable,str(SCRIPT),'--root',str(self.data),'--workspace',str(self.workspace),'--host-id',host]+(['--subject',subject] if subject else [])
 def call(self,name,value,host='codex',subject=None,code=0):
  p=subprocess.run(self.argv(host,subject)+['call',name],input=json.dumps(value),text=True,capture_output=True,timeout=80)
  self.assertEqual(p.returncode,code,p.stdout+p.stderr);return json.loads(p.stdout if code==0 else p.stderr)

 def setup_plan(self,delay=0):
  self.worker=self.workspace/'check.py';self.worker.write_text('import pathlib,sys,time\ntime.sleep('+str(delay)+')\np=pathlib.Path("attempts.txt");p.write_text(p.read_text()+"x" if p.exists() else "x")\npathlib.Path("result.txt").write_text("actual output")\nsys.exit(0 if pathlib.Path("ready").exists() else 1)\n')
  (self.workspace/'.app-delivery-checks.json').write_text(json.dumps({'install':{'argv':[sys.executable,str(self.worker)],'timeout_seconds':5,'artifacts':['result.txt'],'inputs':['check.py']}}))
  return self.call('app_init',{'project_id':'tutorial','goal':'Run a registered installation check','requirements':[{'id':'install','title':'Produces a usable result','check_id':'install'}]})
 def test_failure_fix_and_stale_evidence(self):
  self.setup_plan();failed=self.call('app_run_check',{'project_id':'tutorial','check_id':'install','expected_revision':1});self.assertEqual(failed['result']['status'],'FAIL');self.assertFalse(failed['project']['accepted'])
  (self.workspace/'ready').touch();passed=self.call('app_run_check',{'project_id':'tutorial','check_id':'install','expected_revision':3});self.assertTrue(passed['project']['accepted']);self.assertEqual(passed['result']['exit_code'],0)
  self.worker.write_text(self.worker.read_text()+'# source changed\n');self.assertEqual(self.call('app_status',{'project_id':'tutorial'})['results']['install']['status'],'STALE')
  self.assertEqual(self.call('app_run_check',{'project_id':'tutorial','check_id':'unregistered','expected_revision':5},code=2)['code'],'UNKNOWN_CHECK')
 def test_host_exit_recovers_original_run(self):
  self.setup_plan(.6);(self.workspace/'ready').touch();p=subprocess.Popen(self.argv()+['call','app_run_check'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);p.stdin.write(json.dumps({'project_id':'tutorial','check_id':'install','expected_revision':1}));p.stdin.close()
  deadline=time.monotonic()+5
  while not list((self.data/'runs').glob('*/request.json')) if (self.data/'runs').exists() else True:
   self.assertLess(time.monotonic(),deadline);time.sleep(.03)
  time.sleep(.15);p.kill();p.wait();p.stdout.close();p.stderr.close();time.sleep(.8)
  result=self.call('app_status',{'project_id':'tutorial'});self.assertTrue(result['accepted'],result);self.assertEqual((self.workspace/'attempts.txt').read_text(),'x');self.assertEqual(len(result['history']),1)
 def test_config_change_and_path_escape(self):
  self.setup_plan();path=self.workspace/'.app-delivery-checks.json';path.write_text(path.read_text()+' ')
  self.assertEqual(self.call('app_run_check',{'project_id':'tutorial','check_id':'install','expected_revision':1},code=2)['code'],'CONFIGURATION_CHANGED')
  path.write_text(json.dumps({'escape':{'argv':['true'],'artifacts':['../outside']}}));self.assertEqual(self.call('app_status',{'project_id':'tutorial'},code=2)['code'],'PATH_OUTSIDE_WORKSPACE')

if __name__=='__main__':unittest.main()
