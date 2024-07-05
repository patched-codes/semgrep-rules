#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/pickle_deserialize.py
# hash:  8eee173

import cPickle
import StringIO

# cPickle
# ruleid: python_deserialization_rule-cpickle
serialized = cPickle.dumps({(): []})
# ruleid: python_deserialization_rule-cpickle
print(cPickle.loads(serialized))

file_obj = StringIO.StringIO()
# ruleid: python_deserialization_rule-cpickle
cPickle.dump((1,), file_obj)
file_obj.seek(0)
# ruleid: python_deserialization_rule-cpickle
print(cPickle.load(file_obj))

file_obj.seek(0)
# ruleid: python_deserialization_rule-cpickle
print(cPickle.Unpickler(file_obj).load())

