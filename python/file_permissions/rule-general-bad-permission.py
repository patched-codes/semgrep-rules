#!/usr/bin/env python
# License: MIT (c) GitLab Inc.

import os

# ruleid: python_file-permissions_rule-general-bad-permission
os.chmod(key_file, 0o777)
# ruleid: python_file-permissions_rule-general-bad-permission
os.chmod('/etc/hosts', 0o777)
# ruleid: python_file-permissions_rule-general-bad-permission
os.chmod('/tmp/oh_hai', 0x1ff)
# ruleid: python_file-permissions_rule-general-bad-permission
os.chmod('/tmp/oh_hai', 0o007)
