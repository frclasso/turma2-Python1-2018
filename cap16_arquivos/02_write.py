#!/usr/bin/env python3

# Abrindo e escrevendo

f = open('teste.txt', 'w')  # escrevendo conteudo, w, write
f.write('Primeira linha')
f.write('\nSegunda linha')
f.write('\nTerceira linha')
f.write('\nQuarta linha')
f.write('\nQuinta linha')
f.write('\nSexta linha')
f.write('\nSetima linha')
f.write('\nOitava linha')
f.write('\nNona linha')
f.write('\nDecima linha')
print(f.closed)