#!/usr/bin/env python3

try:
    fh = open('testfile.txt', 'w')  # mude para w/r
    fh.write('Esse e meu arquivo de teste  para manipulacao  de excessoes.')
except IOError:
    print('Nao foi possivel  encontrar o arquivo  ou ler seus dados')
else:
    print('Conteudo  salvo com sucesso')