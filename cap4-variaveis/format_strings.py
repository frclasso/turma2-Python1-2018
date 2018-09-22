nome = 'Fabio'
code = 'Python'
versao = 2.7000
# place holder
""""% python 2.7,  place holder %s (strings) , %d(inteiros) %f(floats)"""

print('Meu nome eh %s meu codigo eh %s, versao: %d' %
      (nome, code, versao))

#formatn Python versao 3.0
print('Meu nome eh {} meu codigo eh {}, versao\n'
      ' {:.1f}'.format(nome, code,versao))

# versao 3.6.5
# format{}
print(f'Meu nome {nome} meu codigo {code}, versao {versao}')