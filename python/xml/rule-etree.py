#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/xml_lxml.py
# hash:  8eee173

import lxml.etree
import lxml
from lxml import etree
from defusedxml.lxml import fromstring
from defuxedxml import lxml as potato

xmlString = "<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"
root = lxml.etree.fromstring(xmlString)
# ruleid: python_xml_rule-etree
lxml.etree.RestrictedElement()
# ruleid: python_xml_rule-etree
lxml.etree.GlobalParserTLS()
# ruleid: python_xml_rule-etree
lxml.etree.getDefaultParser()
# ruleid: python_xml_rule-etree
lxml.etree.check_docinfo()
root = fromstring(xmlString)
