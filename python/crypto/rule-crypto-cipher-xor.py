#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/ciphers.py
# hash:  8eee173

from Crypto.Cipher import XOR as pycrypto_xor
from Cryptodome.Cipher import XOR as pycryptodomex_xor

key = b'Super secret key'
plaintext = b'Encrypt me'
# ruleid: python_crypto_rule-crypto-cipher-xor
cipher = pycrypto_xor.new(key)
msg = cipher.encrypt(plaintext)
# ruleid: python_crypto_rule-crypto-cipher-xor
cipher = pycryptodomex_xor.new(key)
msg = cipher.encrypt(plaintext)

