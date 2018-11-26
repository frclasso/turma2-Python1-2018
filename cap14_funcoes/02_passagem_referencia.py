#!/usr/bin/env python3

# Estamos alterando a lista original, passagem por REFERENCIA

def changeme(mylist):
    """Altera uma lista passada como argumento de função"""

    print("Valores dentro da funcao ANTES da mudanca", mylist)
    mylist[2] = 50
    print("Valores dentro da funcao DEPOIS da mundanca", mylist)
    return


mylist = [10,20,30]

# Chamando a funcao
changeme(mylist)

# Fora da funcao
print(mylist)