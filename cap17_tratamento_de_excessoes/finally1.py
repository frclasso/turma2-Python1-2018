#!/usr/bin/env python3

try:
    fh = open('testefile.txt', 'w')
    fh.writelines('Esse é meu arquivo teste para manipulacao de excessoes')
finally:
    print('Nao foi possivel encontrar o arquivo ou ler os seus dados')
fh.close()
