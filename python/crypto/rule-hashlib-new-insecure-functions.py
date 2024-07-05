#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/hashlib_new_insecure_functions.py
# hash:  8eee173

import hashlib

# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new('md5')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new('md4', 'test')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new(name='md5', string='test')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new('MD4', string='test')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new(string='test', name='MD5')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new('sha1')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new(string='test', name='SHA1')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new('sha', string='test')
# ruleid: python_crypto_rule-hashlib-new-insecure-functions
hashlib.new(name='SHA', string='test')

# Test that plugin does not flag valid hash functions.
hashlib.new('sha256')
hashlib.new('SHA512')

