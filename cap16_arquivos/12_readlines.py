#!/usr/bin/env python3

f = open('teste.txt', 'r')
line = f.readlines()
for l in line:
    print('Lendo linhas:', l, end='')
f.close()