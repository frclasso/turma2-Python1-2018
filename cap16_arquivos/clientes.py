#!/usr/bin/env python3

print()
print('-'* 90)
print('-'* 33, 'Hotel Floripa Paradise', '-'*35)
print()


clientes = [
    ('211112233', {'sobrenome':'Classo', 'nome':'Fabio', 'idade':44, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' }),
    ('23112233', {'sobrenome':'Souza', 'nome':'Amanda', 'idade':40, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' }),
    ('32112233', {'sobrenome':'Pereira', 'nome':'Joana', 'idade':34, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' }),
    ('12112233', {'sobrenome':'Vasquez', 'nome':'Andre', 'idade':24, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' }),
    ('42112233', {'sobrenome':'Silva', 'nome':'Juliana', 'idade':14, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' }),
    ('52112233', {'sobrenome':'Ferreira', 'nome':'Giovana', 'idade':54, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' }),
    ('62112233', {'sobrenome':'Orleans', 'nome':'Erick', 'idade':64, 'sexo':'M',
                  'cpf':'045045045045', 'telefone':'99998888', 'email':'fabio@email.com' })
]
# for ID, dados in clientes:
#     print(ID, dados['sobrenome'], ',',dados['nome'], ',', dados['idade'])

# ordenando sorted
# for ID, dados in sorted(clientes, reverse=True):
#     print(ID, dados['sobrenome'], ',',dados['nome'], ',', dados['idade'])

# ordenar nome - key=lambda clientes:clientes[]
# for ID, dados in sorted(clientes,key=lambda clientes:clientes[1]['idade'],reverse=False):
#     print(ID, dados['sobrenome'], ',',dados['nome'], ',', dados['idade'])

with open('clientes.txt', 'w') as f:
    for ID, dados in clientes:
        f.write('\n{},{},{},{},{},{},{},{}'.format(ID, dados['sobrenome'], dados['nome'], dados['idade'],
                                            dados['sexo'], dados['cpf'], dados['telefone'],
                                            dados['email']))

import csv

with open('clientes.csv', 'w') as f2:
    for ID, dados in clientes:
        csv_file = csv.writer(f2)
        f2.write('\n{},{},{},{},{},{},{},{}'.format(ID, dados['sobrenome'], dados['nome'], dados['idade'],
                                                   dados['sexo'], dados['cpf'], dados['telefone'],
                                                   dados['email']))


