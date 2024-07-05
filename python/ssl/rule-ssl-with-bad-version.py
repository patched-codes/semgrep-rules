# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/ssl-insecure-version.py
# hash:  8eee173

import ssl
from pyOpenSSL import SSL

# ruleid: python_ssl_rule-ssl-with-bad-version
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_SSLv2)
# ruleid: python_ssl_rule-ssl-with-bad-version
SSL.Context(method=SSL.SSLv2_METHOD)
# ruleid: python_ssl_rule-ssl-with-bad-version
SSL.Context(method=SSL.SSLv23_METHOD)

# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(ssl_version=ssl.PROTOCOL_SSLv2)
# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(method=SSL.SSLv2_METHOD)
# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(method=SSL.SSLv23_METHOD)

# strict tests
# ruleid: python_ssl_rule-ssl-with-bad-version
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_SSLv3)
# ruleid: python_ssl_rule-ssl-with-bad-version
ssl.wrap_socket(ssl_version=ssl.PROTOCOL_TLSv1)
# ruleid: python_ssl_rule-ssl-with-bad-version
SSL.Context(method=SSL.SSLv3_METHOD)
# ruleid: python_ssl_rule-ssl-with-bad-version
SSL.Context(method=SSL.TLSv1_METHOD)

# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(ssl_version=ssl.PROTOCOL_SSLv3)
# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(ssl_version=ssl.PROTOCOL_TLSv1)
# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(method=SSL.SSLv3_METHOD)
# ruleid: python_ssl_rule-ssl-with-bad-version
herp_derp(method=SSL.TLSv1_METHOD)

ssl.wrap_socket()

# ruleid: python_ssl_rule-ssl-with-bad-version
def open_ssl_socket(version=ssl.PROTOCOL_SSLv2):
    pass

# ruleid: python_ssl_rule-ssl-with-bad-version
def open_ssl_socket(version=SSL.SSLv2_METHOD):
    pass

# ruleid: python_ssl_rule-ssl-with-bad-version
def open_ssl_socket(version=SSL.SSLv23_METHOD):
    pass

# this one will pass ok
# ruleid: python_ssl_rule-ssl-with-bad-version
def open_ssl_socket(version=SSL.TLSv1_1_METHOD):
    pass
