#!/usr/bin/env python3

# Variavel global
a = 5

def muda_valor():
    #global a  # Altera o valor em todos os ESCOPOS/GLOBALMENTE
    a = 7  # var local
    print(f'a dentro da funcao:{a}')
    return

# Chamando a funcao
muda_valor()

# Fora da funcao
print(f'Fora da funcao:{a}')

