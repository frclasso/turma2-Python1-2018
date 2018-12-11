#1/usr/bin/env python3

import sys


def linux_interaction():
    assert ('linux' in sys.platform), 'Function can only run on linux system'
    print('Doing something')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')
else:
    print('Executing else clause.')