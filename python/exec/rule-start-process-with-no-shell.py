# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/os-spawn.py
# hash:  8eee173

import os

# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnl(mode, path)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnle(mode, path, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnlp(mode, file)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnlpe(mode, file, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnv(mode, path, args)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnve(mode, path, args, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnvp(mode, file, args)
# ruleid: python_exec_rule-start-process-with-no-shell
os.spawnvpe(mode, file, args, env)

# ruleid: python_exec_rule-start-process-with-no-shell
os.execl(path, arg0, arg1)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execle(path, arg0, arg1, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execlp(file, arg0, arg1)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execlpe(file, arg0, arg1, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execv(path, args)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execve(path, args, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execvp(file, args)
# ruleid: python_exec_rule-start-process-with-no-shell
os.execvpe(file, args, env)
# ruleid: python_exec_rule-start-process-with-no-shell
os.startfile(file, args, env)
