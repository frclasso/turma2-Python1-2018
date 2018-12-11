#!/usr/bin/env python3

f = open("teste.txt", 'r+')
str = f.read(40)
print('Read string is: ', str)
print()
# Checando a posicao atual do cursor
position = f.tell()
print("Current file position:", position)
print()
# colocando o cursor no inicio do arquivo
#position = f.seek(0,0,)  # redefine a posicao, inicio do arquivo

# Checando a posicao atual do cursor
print("Current file position:", position)
print()
str = f.read()
print('Again read the string:', str)

# fechando
f.close()