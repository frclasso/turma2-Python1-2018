#!/usr/bin/env python3

try:
    a = int(input('Digite um numero inteiro:'))
    b = int(input('Digite outro numero inteiro:'))

    print("{} / {} = {}".format(a, b, a/b))

except ZeroDivisionError:
    print('O segundo numero nao poder ser Zero')