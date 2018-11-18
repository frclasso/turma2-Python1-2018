#!/usr/bin/env python3


import time
t = (2016, 2 ,15, 10, 13, 38, 1, 48, 0)

d = time.mktime(t)
print('Time mktime %f' % d)

print(time.asctime(time.localtime(d)))