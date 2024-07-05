# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/wildcard-injection.py
# hash:  8eee173

import os as o
import os
import subprocess
import subprocess as subp
import sys

# Vulnerable to wildcard injection
# ruleid: python_exec_rule-linux-command-wildcard-injection
o.system("/bin/tar xvzf *")
# ruleid: python_exec_rule-linux-command-wildcard-injection
o.system('/bin/chown *')
# ruleid: python_exec_rule-linux-command-wildcard-injection
o.popen('/bin/chmod *')
# ruleid: python_exec_rule-linux-command-wildcard-injection
subp.Popen('/bin/chown *', shell=True)

# Not vulnerable to wildcard injection
# rule ok: python_exec_rule-linux-command-wildcard-injection
subp.Popen('/bin/rsync *')
# rule ok: python_exec_rule-linux-command-wildcard-injection
subp.Popen("/bin/chmod *")
# rule ok: python_exec_rule-linux-command-wildcard-injection
subp.Popen(['/bin/chown', '*'])
# rule ok: python_exec_rule-linux-command-wildcard-injection
subp.Popen(["/bin/chmod", sys.argv[1], "*"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# rule ok: python_exec_rule-linux-command-wildcard-injection
o.spawnvp(os.P_WAIT, 'tar', ['tar', 'xvzf', '*'])

# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system("tar *")
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("chmod 777 *")
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("chown root:root *")
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("rsync -avz * destination/")
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("tar cvf archive.tar *")

# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system("tar *")
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("chmod 777 *", 'r', -1)
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("chown root:root *", 'r', -1)
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("rsync -avz * destination/", 'r', -1)
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.popen("tar cvf archive.tar *", 'r', -1)

# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("tar *", shell=True, stdout=subprocess.PIPE)
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("chmod 777 *", shell=True, stderr=subprocess.PIPE)
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("chown root:root *", shell=True, stdin=subprocess.PIPE)
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("rsync -avz * destination/", shell=True, cwd="/tmp")

# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("tar abc?", shell=True)
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("chmod 777 secret?.txt", shell=True)
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("chown root:root secret?.txt", shell=True)
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("rsync -avz secret?.txt destination/", shell=True)
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system("cat secret?.txt")

# ruleid: python_exec_rule-linux-command-wildcard-injection
stdout, stderr = subprocess.Popen('ls -la *', shell=True, stdout=subprocess.PIPE, text=True).communicate()
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system('grep "some_search_term" *.py')
options = {"stdout": subprocess.PIPE}
# rule ok: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("ls", shell=True, **options)
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system("ls *.txt")
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system('grep "some_search_term" *.py')
# ruleid: python_exec_rule-linux-command-wildcard-injection
subprocess.Popen("rm *.tmp", shell=True)
# ruleid: python_exec_rule-linux-command-wildcard-injection
os.system("tar czf logs.tar.gz *.log")