#!/usr/bin/env python3

try:
    try:
        x = int(input('Digite um numero: '))
    finally:
        print('Restabelecendo um novo valor para x')
        x = None
except:
    print('Ocorreu algum erro')
