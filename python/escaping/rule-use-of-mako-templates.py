# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/mako_templating.py
# hash:  8eee173

from mako.template import Template
from mako.lookup import TemplateLookup
import mako

from mako import template

# ruleid: python_escaping_rule-use-of-mako-templates
Template("hello")

# XXX(fletcher): for some reason, bandit is missing the one below. keeping it
# in for now so that if it gets fixed inadvertently we know.
# ruleid: python_escaping_rule-use-of-mako-templates
mako.template.Template("hern")

# Disable default filters so no filters are applied.
# ruleid: python_escaping_rule-use-of-mako-templates
template.Template("hern", default_filters=[])

# rule ok: python_escaping_rule-use-of-mako-templates
template = Template("hern", default_filters=['h'])  # 'h' is the HTML escape filter

# ruleid: python_escaping_rule-use-of-mako-templates
TemplateLookup(directories=['/tmp'])

# rule ok: python_escaping_rule-use-of-mako-templates
TemplateLookup(directories=['/tmp'], default_filters=['h'])  # 'h' is the HTML escape filter

# Disable default filters so no filters are applied.
# ruleid: python_escaping_rule-use-of-mako-templates
TemplateLookup(directories=['/tmp'], default_filters=[])