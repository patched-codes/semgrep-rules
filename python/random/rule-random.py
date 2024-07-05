#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/random_module.py
# hash:  8eee173

import random
import os
import somelib

# ruleid: python_random_rule-random
bad = random.random()
# ruleid: python_random_rule-random
bad = random.randrange()
# ruleid: python_random_rule-random
bad = random.randint()
# ruleid: python_random_rule-random
bad = random.choice()
# ruleid: python_random_rule-random
bad = random.uniform()
# ruleid: python_random_rule-random
bad = random.triangular()

good = os.urandom()
good = random.SystemRandom()

unknown = random()
unknown = somelib.a.random()
