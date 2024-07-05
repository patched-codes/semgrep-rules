#!/usr/bin/env python
# License: MIT (c) GitLab Inc.

import dill

cube = lambda x: x * x *x
# ruleid: python_deserialization_rule-dill
pickle_answer = dill.dumps(cube)
print(pickle_answer)
