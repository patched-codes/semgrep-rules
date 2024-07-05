#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/crypto-md5.py
# hash:  8eee173

import hashlib

# ruleid: python_crypto_rule-hash-md5
hashlib.md5(1)
# ruleid: python_crypto_rule-hash-md5
hashlib.md5(1).hexdigest()

# ruleid: python_crypto_rule-hash-md5
abc = str.replace(hashlib.md5("1"), "###")

# ruleid: python_crypto_rule-hash-md5
print(hashlib.md5("1"))

