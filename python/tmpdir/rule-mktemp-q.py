#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/mktemp.py
# hash:  8eee173

from tempfile import mktemp
import tempfile.mktemp as mt
import tempfile as tmp

foo = 'hi'

# ruleid: python_tmpdir_rule-mktemp-q
mktemp(foo)
# ruleid: python_tmpdir_rule-mktemp-q
tempfile.mktemp('foo')
# ruleid: python_tmpdir_rule-mktemp-q
mt(foo)
# ruleid: python_tmpdir_rule-mktemp-q
tmp.mktemp(foo)
