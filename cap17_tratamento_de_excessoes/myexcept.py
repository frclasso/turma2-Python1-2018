#!/usr/bin/env python3

try:
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    print('{}/{} = {}'.format(a,b,a/b))
except ZeroDivisionError:
    print('O segundo numero nao pode ser Zero')
# except ValueError:
#     print('O valor fornecido precisa ser um inteiro')
except Exception as e:
    print('Erro desconhecido', e)
    raise
