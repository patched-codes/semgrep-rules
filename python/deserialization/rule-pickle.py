#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/pickle_deserialize.py
# hash:  8eee173

import _pickle
import pickle
import os

# pickle
pick = pickle.dumps({'a': 'b', 'c': 'd'})

with open('serialized.pkl', 'wb') as file:
    pickle.dump([1, 2, '3'], file)

# Unpickle
# ruleid: python_deserialization_rule-pickle
print(pickle.loads(pick))
# ruleid: python_deserialization_rule-pickle
print(_pickle.loads(pick))

with open('serialized.pkl', 'rb') as file:
    # ruleid: python_deserialization_rule-pickle
    print(pickle.load(file))

with open('serialized.pkl', 'rb') as file:
    # ruleid: python_deserialization_rule-pickle
    print(_pickle.load(file))

with open('serialized.pkl', 'rb') as file:
    # ruleid: python_deserialization_rule-pickle
    print(pickle.Unpickler(file).load())

with open('serialized.pkl', 'rb') as file:
    # ruleid: python_deserialization_rule-pickle
    print(_pickle.Unpickler(file).load())

# Delete the file "serialized.pkl"
os.remove('serialized.pkl')

# This will run the following command and list all the directories: ls ~
# But this is okay because this string is not controlled by the attacker.
# And so hard-coded strings are okay.
# ok: python_deserialization_rule-pickle
pickle.loads(b"cos\nsystem\n(S\'ls ~\'\ntR.")

aa = ["a", 'b', 3]
# ruleid: python_deserialization_rule-pickle
print(pickle.loads(pickle.dumps(aa)))
