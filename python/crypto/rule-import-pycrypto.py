#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/pycrypto.py
# hash:  8eee173

# ruleid: python_crypto_rule-import-pycrypto
import Crypto.Cipher
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.Hash
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.IO
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.Protocol
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.PublicKey
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.Random
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.Signature
# ruleid: python_crypto_rule-import-pycrypto
import Crypto.Util

from . import CryptoMaterialsCacheEntry

def test_pycrypto():
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = pycrypto_arc2.new(key, AES.MODE_CFB, iv)
    factory = CryptoMaterialsCacheEntry()


def test_pycrypto():
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = pycrypto_arc2.new(key, AES.MODE_CFB, iv)
    factory = CryptoMaterialsCacheEntry()
