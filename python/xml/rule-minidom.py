#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/xml_minidom.py
# hash:  8eee173

from xml.dom.minidom import parseString as badParseString
from defusedxml.minidom import parseString as goodParseString

from xml.dom.minidom import parse as badParse
from defusedxml.minidom import parse as goodParse

def foo(str):
  # ruleid: python_xml_rule-minidom
  a = badParseString(str)
  print(a)
  # ok: python_xml_rule-minidom
  b = goodParseString(str)
  print(b)

  # ruleid: python_xml_rule-minidom
  a = badParse(str)
  print(a)
  # ok: python_xml_rule-minidom
  b = goodParse(str)
  print(b)
