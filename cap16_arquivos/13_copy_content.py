#!/usr/bin/env python3

with open('foo.txt', 'r') as f:
    with open('foo_copy.txt', 'w') as wf:
        for line in f:
            wf.write(line)
print('Done...')
