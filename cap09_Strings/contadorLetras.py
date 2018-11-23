#!/usr/bin/env python3

fruta = 'banana'
contador = 0
for letra in fruta:
    if letra == 'a':
        contador += 1
print(f'Encontramos: {contador} vezes.')

"""Utilizando  a função str"""

fruta == 'abacaxi'
print(str.count(fruta, 'a'))