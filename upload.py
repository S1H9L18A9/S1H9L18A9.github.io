import os
import subprocess

run_cmd = lambda x:subprocess.Popen(x)

subprocess.Popen(['landslide','-c','-r','test.md','-d','index.html'])
subprocess.Popen(['git','add','.'])
subprocess.Popen(['git','commit','-a','-m','"commit"'])
subprocess.Popen(['git','push'])
