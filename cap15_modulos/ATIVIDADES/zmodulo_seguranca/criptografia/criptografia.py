#!/usr/bin/env python3

"""Desevolver uma aplicação de criptografia"""


# https://pymotw.com/2/hashlib/index.html

# Melhorar:
# Decriptografa
# Duas funcoes
# nome do arquivo de saida, usar data
print('Programa criptografia importado com sucesso')

def criptografa():
    try:
        arquivo = input('Selecione um arquivo a ser criptografado: ')
        with open (arquivo, mode='r') as f:
            cripto = str(f.read())
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

        criptografado = cripto

        with open('textocriptografado.txt', 'w') as f2:# write
            for x in criptografado:
                f2.write(x)

        print('Arquivo criptogrfado com sucesso!')

    except FileNotFoundError:
        print('Arquivo nao encontrado')


def decriptografa():
    try:
        arquivo = input('Selecione um arquivo a ser decriptografado: ')
        with open (arquivo, mode='r') as f:
            decripto = str(f.read())
            for l in decripto:
                if l == '3':
                    decripto = decripto.replace('3', 'e')
                if l == '@':
                    decripto = decripto.replace('@', 'a')
                if l == '%':
                    decripto = decripto.replace('%', 'x')
                if l == '0':
                    decripto = decripto.replace('0', 'o')
                if l == '8':
                    decripto = decripto.replace('8', 'g')

        decriptografado = decripto

        with open('textoDecriptografado.txt', 'w') as f2:# write
            for x in decriptografado:
                f2.write(x)

        print('Arquivo DECRIPTOGRAFADO com sucesso!')

    except FileNotFoundError:
        print('Arquivo nao encontrado')


#criptografa()

#decriptografa()