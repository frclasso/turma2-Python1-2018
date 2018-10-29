#!/usr/bin/env python3

"""Desevolver uma aplicação de criptografia"""


# https://pymotw.com/2/hashlib/index.html


str = 'Texto sem criptografia'
textoCriptografado = str.replace('e', '3')
textoCriptografado2 = textoCriptografado
textoCriptografado2.replace('a', '@')
print(textoCriptografado2)
