# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/requests-ssl-verify-disabled.py
# hash:  8eee173

import requests

requests.get('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.get('https://gmail.com', verify=False)
requests.post('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.post('https://gmail.com', verify=False)
requests.put('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.put('https://gmail.com', verify=False)
requests.delete('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.delete('https://gmail.com', verify=False)
requests.patch('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.patch('https://gmail.com', verify=False)
requests.options('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.options('https://gmail.com', verify=False)
requests.head('https://gmail.com', verify=True)
# ruleid: python_ssl_rule-req-no-certvalid
requests.head('https://gmail.com', verify=False)
