# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/jinja2_templating.py
# hash:  8eee173

import jinja2
from jinja2 import Environment, select_autoescape
templateLoader = jinja2.FileSystemLoader( searchpath="/" )
something = ''

Environment(loader=templateLoader, load=templateLoader, autoescape=True)
templateEnv = jinja2.Environment(autoescape=True,
        loader=templateLoader )
# ruleid: python_escaping_rule-jinja2-autoescape-false
Environment(loader=templateLoader, load=templateLoader, autoescape=something)
# ruleid: python_escaping_rule-jinja2-autoescape-false
templateEnv = jinja2.Environment(autoescape=False, loader=templateLoader )
# ruleid: python_escaping_rule-jinja2-autoescape-false
Environment(loader=templateLoader,
            load=templateLoader,
            autoescape=False)

# ruleid: python_escaping_rule-jinja2-autoescape-false
Environment(loader=templateLoader,
            load=templateLoader)

Environment(loader=templateLoader, autoescape=select_autoescape())

Environment(loader=templateLoader,
            autoescape=select_autoescape(['html', 'htm', 'xml']))


def fake_func():
    return 'foobar'
# ruleid: python_escaping_rule-jinja2-autoescape-false
Environment(loader=templateLoader, autoescape=fake_func())
