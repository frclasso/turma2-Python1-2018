#!/usr/bin/env python3

f = open('foo.txt', 'r')
print('Nome do arquivo:', f.name)
for index in range(6):
    line = next(f)
    print(f'Line number {index} - {line}',end='')
f.close()