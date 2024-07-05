#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/crypto-md5.py
# hash:  8eee173

from Crypto.Hash import MD4 as pycrypto_md4
from Cryptodome.Hash import MD4 as pycryptodomex_md4

# ruleid: python_crypto_rule-hash-md4
pycrypto_md4.new()

# ruleid: python_crypto_rule-hash-md4
pycryptodomex_md4.new()
