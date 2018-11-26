#!/usr/bin/env python3

"""Sempre que usamos a palavra reservada yield , estamos criando uma funcao
geradora. A funcao geradora gera um valor toda vez em que e “chamada”, e aqui,
usamos aspas, pois não e uma chamada comum. Por padrão, as funções geradoras
podem ser iteradas no comando for"""

def get_generator():
    for i in range(10):
        yield i

for number in get_generator():
    print(number, end=",")

print()
# Usando o return
# Precisamos antes salvar em uma lista
def get_list():
    numbers = []
    for i in range(10):
        numbers.append(i)
    return numbers


for number in get_list():
    print(number,end=',')