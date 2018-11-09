#!/usr/bin/env python3

"""Desenvolver um gerador de senhas coma função random"""

"""https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar"""


import random

# minusculas = ('abcdefghijklmnopqrstuvwxz')
# #print(minusculas)
# maiusculas = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# #print(maiusculas)
#
# senha = []
# for i in range(7):
#     #print(random.choices(minusculas))
#     s = random.choices(minusculas)
#     senha.append(s)
#
# for i in range(7):
#     s = random.choices(maiusculas)
#     senha.append(s)
#
# for i in range(7):
#     n =  random.randint(0, 9)
#     senha.append(n)
#
# print(senha)
# #
# # for c in senha:
# #     print(c, end='')


minusculas = ('abcdefghijklmnopqrstuvwxz')
maiusculas = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = range(10)
simbolos = ('!@#$%^&*')

hard_senha = []
for m in maiusculas:
    hard_senha.append(m)
    for a in maiusculas:
        hard_senha.append(a)
        for n in num:
            hard_senha.append(n)
            for s in simbolos:
                hard_senha.append(s)

print(hard_senha)