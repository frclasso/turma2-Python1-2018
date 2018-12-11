#!/usr/bin/env python3


f = open('teste.txt', 'r') #read
str = f.read(48)  # define a quantidade de caracteres a serem lidos
print(str)
print('Done...')
f.close()