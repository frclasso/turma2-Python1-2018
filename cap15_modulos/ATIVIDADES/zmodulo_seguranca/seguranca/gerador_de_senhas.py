#!/usr/bin/env python3

"""Desenvolver um gerador de senhas coma função random"""

"""https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar"""
import random


print('Modulo gerador de senhas importado com sucesso')


def gerSenha():

    minusculas = 'abcdefghijklmnopqrstuvwxz'
    maiusculas = minusculas.upper()
    numeros = '0123456789' # str(range(10))
    simbolos = '!@#$%^&*'

    senha = []

    for i in range(5):
        s = random.choice(minusculas)
        senha.append(s)

    for i in range(5):
        s = random.choice(maiusculas)
        senha.append(s)

    for i in range(5):
        n = random.choice(numeros)
        senha.append(n)

    for i in range(5):
        s = random.choice(simbolos)
        senha.append(s)


    # print(senha)

    '''Aqui tinha um problema, gerando pares iguais maiusculos, 
    minusculos, numeros e simbolos. '''

    s = ''.join(senha)
    print(s)

    # Resolvendo, gerando outra lista e mais random

    novaSenha = []
    for i in senha:
        for x in i:
            s = random.choice(senha)
        novaSenha.append(s)
    s2 = ''.join(novaSenha)
    print(s2)


# Melhorar: criar funcao que receba o tamanho da senha
# quantidade de elementos

gerSenha()