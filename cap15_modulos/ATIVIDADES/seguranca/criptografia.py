#!/usr/bin/env python3

"""Desevolver uma aplicação de criptografia"""


# https://pymotw.com/2/hashlib/index.html


str = 'Texto sem criptografia'
for l in str:
    if l == 'e':
        str = str.replace('e', '3')
    if l == 'a':
        str = str.replace('a', '@')
    if l == 'x':
        str = str.replace('x', '%')
    if l == 'o':
        str = str.replace('o', '0')
    if l == 'g':
        str = str.replace('g', '8')
    if l == ' ':
        str = str.replace(' ', '*')
print(str)