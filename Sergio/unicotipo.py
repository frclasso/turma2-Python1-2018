#!/usr/bin/env python3

def testaStr():
    """ O input aceita int e float e converte em str, sempre vair ser string."""
    try:
        var1 = input('Entre com uma variavel do tipo string:')
        if type(var1) == str:
            print('Isso eh uma string')
            print(type(var1), var1)
    except ValueError:
        print('Nao eh uma string')  #NUNCA VAI OCORRER, SEMPRE SERA STRING


def testaFloat():
    """class float aceita int e converte em float, mas nao aceita str"""
    try:
        var2 = float(input('Entre com uma variavel do tipo float:'))
        if type(var2) == float:
            print('Float')
            print(type(var2), var2)
    except ValueError:
        print('Nao eh float')


def testaInt():
    """ class int aceita float e int, mas nao aceita str"""
    try:
        var3 = int(input('Entre com uma variavel do tipo inteiro:'))
        if type(var3) == int:
            print('Inteiro')
            print(type(var3), var3)
    except ValueError:
        print('Nao eh inteiro')

testaFloat()
testaInt()
testaStr()
