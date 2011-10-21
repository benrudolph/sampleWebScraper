#!/usr/bin/env python

import sys
import os
import urllib2 #Python module for making web requests 
import re #Python module for using regular expressions

BASE_SITE = 'http://news.ycombinator.com/'
TIMEOUT = 15

request = urllib2.Request(BASE_SITE)
page = None
try:
    handler = urllib2.urlopen(request, timeout=TIMEOUT)
    page = handler.read()
    handler.close();
except IOError:
    print 'Failure to open site'
    sys.exit(0)

linkPattern = r'href="(.*?)"'
linkRe = re.compile(linkPattern)

matchLinks = linkRe.findall(page)

print matchLinks
