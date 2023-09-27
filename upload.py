import os
import subprocess

run_cmd = lambda x:subprocess.Popen(x)
# os.

subprocess.Popen(['landslide','-c','-r','test.md','-d','index.html']).communicate()
subprocess.Popen(['git','add','.']).communicate()
subprocess.Popen(['git','commit','-a','-m','"commit"']).communicate()
subprocess.Popen(['git','push']).communicate()
print('Updated')
# subprocess.Popen(['landslide','-c','-r','test.md','-d','index.html'],stdout=subprocess.PIPE)
# subprocess.Popen(['git','add','.'],stdout=subprocess.PIPE)
# subprocess.Popen(['git','commit','-a','-m','"commit"'],stdout=subprocess.PIPE)
# subprocess.Popen(['git','push'],stdout=subprocess.PIPE)