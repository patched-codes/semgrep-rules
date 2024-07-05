#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/xml_etree_celementtree.py
# hash:  8eee173

import xml.etree.cElementTree as badET
import defusedxml.cElementTree as goodET

xmlString = "<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"

# unsafe
tree = badET.fromstring(xmlString)
print(tree)
# ruleid: python_xml_rule-celement
badET.parse('filethatdoesntexist.xml')
# ruleid: python_xml_rule-celement
badET.iterparse('filethatdoesntexist.xml')
# ruleid: python_xml_rule-celement
a = badET.XMLParser()

# safe
tree = goodET.fromstring(xmlString)
print(tree)
# ok: python_xml_rule-celement
goodET.parse('filethatdoesntexist.xml')
# ok: python_xml_rule-celement
goodET.iterparse('filethatdoesntexist.xml')
# ok: python_xml_rule-celement
a = goodET.XMLParser()

