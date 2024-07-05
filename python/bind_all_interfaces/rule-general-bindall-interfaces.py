# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/binding.py
# hash:  8eee173

import socket

# ruleid: python_bind-all-interfaces_rule-general-bindall-interfaces
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 31137))
s.bind(('192.168.0.1', 8080))
