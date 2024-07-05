# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/hardcoded-tmp.py
# hash:  8eee173

# ruleid: python_tmpdir_rule-hardcodedtmp
with open('/tmp/abc', 'w') as f:
    f.write('def')

# ok
with open('/abc/tmp', 'w') as f:
    f.write('def')

# Negative test
with open('/foo/bar', 'w') as f:
    f.write('def')
