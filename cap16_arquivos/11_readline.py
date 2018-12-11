#!/usr/bin/env python3

f = open('teste.txt', 'r')
line = f.readline()
print('Lendo liha:', line)
line = f.readline(15)
print('Lendo liha:', line)
line = f.readline(15)
print('Lendo liha:', line)
f.close()