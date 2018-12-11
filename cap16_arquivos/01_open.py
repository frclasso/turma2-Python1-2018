#!/usr/bin/env python3

f = open('teste.txt', 'w') # w = write, escrita, se nao existe , cria

print('Nome do arquivo:', f.name)
print('Modo de abertura:', f.mode)
print('Verifica se esta fechado: ',f.closed) # retorna True se estiver fechado
print('Done...')
