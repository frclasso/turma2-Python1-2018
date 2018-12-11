#!/usr/bin/env python3

import urllib.request

try:
    webpage = urllib.request.urlopen('http://www.googles.com')
except:
    print('Could not access the page')
else:
    for line in webpage:
        print(line)