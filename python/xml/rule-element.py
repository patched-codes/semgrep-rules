#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/xml_etree_elementtree.py
# hash:  8eee173

import xml.etree.ElementTree as badET
import defusedxml.ElementTree as goodET

xmlString = "<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"

# unsafe
tree = badET.fromstring(xmlString)
print(tree)
# ruleid: python_xml_rule-element
badET.parse('filethatdoesntexist.xml')
# ruleid: python_xml_rule-element
badET.iterparse('filethatdoesntexist.xml')
# ruleid: python_xml_rule-element
a = badET.XMLParser()

# safe
tree = goodET.fromstring(xmlString)
print(tree)
# ok: python_xml_rule-element
goodET.parse('filethatdoesntexist.xml')
# ok: python_xml_rule-element
goodET.iterparse('filethatdoesntexist.xml')
# ok: python_xml_rule-element
a = goodET.XMLParser()
