#!/usr/bin/env python3

# Nao estamos alterando a lista original, passagem por VALOR

def changme(mylist):
    """Altera uma lista passada como argumento de função"""
    mylist = [10,20,30]
    print("Valores dentro da funcao:", mylist)
    return

mylist = [100,200,300]

#Chamando a funcao
changme(mylist)  # 10,20,30

print('Valores, fora da funcao', mylist)