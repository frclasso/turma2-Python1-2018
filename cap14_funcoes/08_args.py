#!/usr/bin/env python3

def printinfo(arg1, *vartuple):  #args
    """Imprime variaveis passadas como argumento"""
    print('Out is:', arg1)
    print('Tupla de valores:',vartuple)
    return

#Chamando a funcao

printinfo(10, 70,60,50)

