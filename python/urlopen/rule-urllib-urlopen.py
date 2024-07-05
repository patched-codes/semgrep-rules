#!/usr/bin/env python
# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/urlopen.py
# hash:  8eee173
import os
import ssl
import urllib
import urllib2

# Python 3
import urllib.request

# Six
import six

ssl._create_default_https_context = ssl._create_unverified_context

# Set up a sample file for tainted input
with open('a123.txt', 'w') as file1:
    file1.write("https://abc.com/")

with open('a123.txt', 'r') as file1:
    url_from_user = file1.read()
filename = 'abc.txt'
http_url = 'http://abc.com'

# urllib
url = urllib.quote('abc.com')
# ok: python_urlopen_rule-urllib-urlopen
urllib.urlopen(http_url)
# ok: python_urlopen_rule-urllib-urlopen
urllib.urlopen("http://abc.com")
# ruleid: python_urlopen_rule-urllib-urlopen
urllib.urlopen(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
urllib.urlretrieve('http://abc.com', 'abc.txt')
# ruleid: python_urlopen_rule-urllib-urlopen
urllib.urlretrieve(url_from_user, 'abc2.txt')

opener = urllib.URLopener()
# ruleid: python_urlopen_rule-urllib-urlopen
opener.open(url_from_user)
# ruleid: python_urlopen_rule-urllib-urlopen
opener.retrieve(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
opener.open('file:///bin/ls')
# ok: python_urlopen_rule-urllib-urlopen
opener.retrieve('file:///bin/ls')

opener = urllib.FancyURLopener()
# ruleid: python_urlopen_rule-urllib-urlopen
opener.open(url_from_user)
# ruleid: python_urlopen_rule-urllib-urlopen
opener.retrieve(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
opener.open('file:///bin/ls')
# ok: python_urlopen_rule-urllib-urlopen
opener.retrieve('file:///bin/ls')

# urllib2
handler = urllib2.HTTPBasicAuthHandler()
handler.add_password(realm='test', uri='http://mysite.com', user='bob', passwd='123')
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
urllib2.urlopen('file:///bin/ls')
urllib2.urlopen(url_from_user)
urllib2.Request('file:///bin/ls')

# Python 3
# ruleid: python_urlopen_rule-urllib-urlopen
urllib.request.urlopen(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
urllib.request.urlopen('file:///bin/ls')
# ruleid: python_urlopen_rule-urllib-urlopen
urllib.request.urlretrieve(url_from_user, 'abc.txt')
# ok: python_urlopen_rule-urllib-urlopen
urllib.request.urlretrieve('file:///bin/ls',filename)

opener = urllib.request.URLopener()
# ruleid: python_urlopen_rule-urllib-urlopen
opener.open(url_from_user)
# ruleid: python_urlopen_rule-urllib-urlopen
opener.retrieve(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
opener.open('file:///bin/ls')
# ok: python_urlopen_rule-urllib-urlopen
opener.retrieve('file:///bin/ls')

opener = urllib.request.FancyURLopener()
# ruleid: python_urlopen_rule-urllib-urlopen
opener.open(url_from_user)
# ruleid: python_urlopen_rule-urllib-urlopen
opener.retrieve(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
opener.open('file:///bin/ls')
# ok: python_urlopen_rule-urllib-urlopen
opener.retrieve('file:///bin/ls')

# Six
six.moves.urllib.request.urlopen('file:///bin/ls')
six.moves.urllib.request.urlretrieve('file:///bin/ls', 'abc3.txt')

opener = six.moves.urllib.request.URLopener()
# ruleid: python_urlopen_rule-urllib-urlopen
opener.open(url_from_user)
# ruleid: python_urlopen_rule-urllib-urlopen
opener.retrieve(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
opener.open('file:///bin/ls')
# ok: python_urlopen_rule-urllib-urlopen
opener.retrieve('file:///bin/ls')

opener = six.moves.urllib.request.FancyURLopener()
# ruleid: python_urlopen_rule-urllib-urlopen
opener.open(url_from_user)
# ruleid: python_urlopen_rule-urllib-urlopen
opener.retrieve(url_from_user)
# ok: python_urlopen_rule-urllib-urlopen
opener.open('file:///bin/ls')
# ok: python_urlopen_rule-urllib-urlopen
opener.retrieve('file:///bin/ls')

# Clean up
os.remove('a123.txt')
os.remove('abc.txt')
os.remove('abc2.txt')
os.remove('abc3.txt')
