#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/crypto-md5.py
# hash:  8eee173

from cryptography.hazmat.primitives import hashes

# ruleid: python_crypto_rule-crypto.hazmat-hash-md5
hashes.MD5()
