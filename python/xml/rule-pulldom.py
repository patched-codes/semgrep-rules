#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/xml_minidom.py
# hash:  8eee173

from xml.dom.pulldom import parseString as badParseString
from defusedxml.pulldom import parseString as goodParseString

from xml.dom.pulldom import parse as badParse
from defusedxml.pulldom import parse as goodParse

def foo(str):
  # ruleid: python_xml_rule-pulldom
  a = badParseString(str)
  print(a)
  b = goodParseString(str)
  print(b)

  # ruleid: python_xml_rule-pulldom
  a = badParse(str)
  print(a)
  # ok: python_xml_rule-pulldom
  b = goodParse(str)
  print(b)
