#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/marshal_deserialize.py
# hash:  8eee173

import marshal
import tempfile

# ruleid: python_deserialization_rule-marshal
serialized = marshal.dumps({'a': 1})
# ruleid: python_deserialization_rule-marshal
print(marshal.loads(serialized))

file_obj = tempfile.TemporaryFile()
# ruleid: python_deserialization_rule-marshal
marshal.dump(range(5), file_obj)
file_obj.seek(0)
# ruleid: python_deserialization_rule-marshal
print(marshal.load(file_obj))
file_obj.close()
