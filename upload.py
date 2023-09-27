import os
import subprocess

run_cmd = lambda x:subprocess.Popen(x,stdout=subprocess.PIPE).communicate()
# os.

run_cmd(['landslide','-c','-r','test.md','-d','index.html'])
run_cmd(['git','add','.'])
run_cmd(['git','commit','-a','-m','"commit"'])
run_cmd(['git','push'])
print('Updated')
# subprocess.Popen(['landslide','-c','-r','test.md','-d','index.html'],stdout=subprocess.PIPE)
# subprocess.Popen(['git','add','.'],stdout=subprocess.PIPE)
# subprocess.Popen(['git','commit','-a','-m','"commit"'],stdout=subprocess.PIPE)
# subprocess.Popen(['git','push'],stdout=subprocess.PIPE)