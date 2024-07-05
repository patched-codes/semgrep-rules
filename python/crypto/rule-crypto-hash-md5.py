#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/crypto-md5.py
# hash:  8eee173

from Crypto.Hash import MD5 as pycrypto_md5
from Cryptodome.Hash import MD5 as pycryptodomex_md5

# ruleid: python_crypto_rule-crypto-hash-md5
pycrypto_md5.new()

# ruleid: python_crypto_rule-crypto-hash-md5
pycryptodomex_md5.new()
