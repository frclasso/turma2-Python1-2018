#!/usr/bin/env python3

try:
    fh = open('testefile.txt', 'w')
    try:
        fh.write('Esse e meu arquivo de teste')
    finally:
        print('Fechando o arquivo')
    fh.close()
except IOError:
    print('Nao foi possivel encontrar o arquivo ou ler os seus dados')
