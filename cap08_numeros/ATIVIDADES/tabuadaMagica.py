#!/usr/bin/env python3

"""Desenvolver uma tabuada para ensino infantil."""

print("/" * 70)
print("*"* 20 + " Bem vindo a tabuada mágica!" + "*"* 21)
print("*"* 7 + " Antes de começar, voce sabe o que é um numero inteiro? " + "*"* 6)
print("*"*4 +" Números inteiros são aqueles entre 0 e 9, sem ponto, lembra?"+ "*"*4)
print("/" * 70)
continua = ['S', 'SIM','s', 'sim', 'Sim','Y', 'YES', 'y', 'yes']
sair = ['Nao', 'nao', 'N', 'n','No','no']
resposta = 'S'
while resposta in continua:
    try:
        tabuada = int(input("Qual tabuada voce quer aprender? "))
        for i in range(1, 11):
            print(i, '*', tabuada,'=', i * tabuada)

    except ValueError:
        print('Precisa ser um numero inteiro')
    print('Vamos fazer outra tabuada?')
    resposta = input('Nova tabuda? Sim/Nao/s/n')
    while resposta not in sair and resposta not in continua:
        print('/'* 70)
        print("Voce digitou um valor incorreto:", resposta)
        print("Para continuar digite:('S', 'SIM','s', 'sim', 'Sim','Y', 'YES', 'y', 'yes')")
        print("E para sair, digite:('Nao', 'nao', 'N', 'n','No','no')")
        print()
        resposta = input('Nova tabuda? Sim/Nao/s/n')
    if resposta in sair:
        print("Saindo...")
        break

print("/"* 70)
print("*"* 7 + " Parabéns e muito obirgado por usar a tabuada mágica " + "*"* 7)
print("/"* 70)


