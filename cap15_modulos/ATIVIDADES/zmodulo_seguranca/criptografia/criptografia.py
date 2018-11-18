#!/usr/bin/env python3

"""Desevolver uma aplicação de criptografia"""


# https://pymotw.com/2/hashlib/index.html

f = open('textoclaro.txt', 'r')
# modo r = read(leitura)
# modo w = write(escrita)

cripto = str(f.read()) # f.read() le todo o arquivo
#print(cripto)


#str = 'Texto sem criptografia'

for l in cripto:
    if l == 'e':
        cripto = cripto.replace('e', '3')
    if l == 'a':
        cripto = cripto.replace('a', '@')
    if l == 'x':
        cripto = cripto.replace('x', '%')
    if l == 'o':
        cripto = cripto.replace('o', '0')
    if l == 'g':
        cripto = cripto.replace('g', '8')


print(cripto)

criptografado = cripto

f2 = open('textocriptografado.txt', 'w') # write
for x in criptografado:
    f2.write(x)

# Melhorar:
# Decriptografa
# Duas funcoes
# nome do arquivo de saida, usar data