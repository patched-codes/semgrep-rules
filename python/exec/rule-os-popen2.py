# License: MIT (c) GitLab Inc.

import subprocess
import os
from subprocess import Popen as pop

# ruleid: python_exec_rule-os-popen2
os.system("")
# ruleid: python_exec_rule-os-popen2
os.popen("")
# ruleid: python_exec_rule-os-popen2
os.popen2("")
# ruleid: python_exec_rule-os-popen2
os.popen3("")
# ruleid: python_exec_rule-os-popen2
os.popen4("")
# ruleid: python_exec_rule-os-popen2
popen2.popen2("")
# ruleid: python_exec_rule-os-popen2
popen2.popen3("")
# ruleid: python_exec_rule-os-popen2
popen2.popen4("")
# ruleid: python_exec_rule-os-popen2
popen2.Popen3("")
# ruleid: python_exec_rule-os-popen2
popen2.Popen4("")
# ruleid: python_exec_rule-os-popen2
commands.getoutput("")
# ruleid: python_exec_rule-os-popen2
commands.getstatusoutput("")

