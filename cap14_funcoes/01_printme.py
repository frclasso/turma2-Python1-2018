#!/usr/bin/env python3

# Definicao da funcao
def printme(str):  # Parametro
    """Imprime uma string passada como argumento"""
    print(str)
    return

# Chamada da funcao
printme('Bom dia alunos') # Argumento
printme(printme.__doc__)  # Chama a documentacao da funcao