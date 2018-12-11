#!/usr/bin/env python3

f = open('teste.txt', 'r+')
seq = ['\nDecima Primeira linha\nDecima segunda linha\nDecima terceira linha']
# escreve a sequencia no final do arquivo
f.seek(0,2)
line = f.writelines(seq)

f.close()