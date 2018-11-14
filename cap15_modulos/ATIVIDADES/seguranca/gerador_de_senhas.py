#!/usr/bin/env python3

"""Desenvolver um gerador de senhas coma função random"""

"""https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar"""
import random

minusculas = ('abcdefghijklmnopqrstuvwxz')
m = minusculas.upper()
numeros = ('0','1','2','3','4','5','6','7','8','9')
simbolos = ('!@#$%^&*')

senha = []

for i in range(5):
    s = random.choice(minusculas)
    senha.append(s)

for i in range(5):
    s = random.choice(m)
    senha.append(s)

for i in range(5):
    n = random.choice(numeros)
    senha.append(n)

for i in range(5):
    s = random.choice(simbolos)
    senha.append(s)

s = ''
s = s.join(senha)
print(s)


# Melhorar: criar funcao que receba o tamanho da senha
# quantidade de elementos
