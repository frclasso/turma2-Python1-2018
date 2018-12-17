#!/usr/bin/env python3

import csv

print('Modulo cadastroDeClientes importado com sucesso')

clientes = []


def novoCliente():
    id = input('Insira numero da carteira de identidade:')
    nome = input('Insira o nome completo do usuario:')
    telefone = input('Insira o telefone do usuario:')
    condicao = input('m - para Mensalista, d - para diarista ou h - para horista:')
    clientes.append((id,{'nome':nome, 'telefone':telefone, 'condicao':condicao} ))

    with open('clientes.csv', mode='a') as f:
        csv_file = csv.writer(f)
        f.write('{},{},{},{}\n'.format(id,nome,telefone,condicao))
        print()

    return f'ID:{id} - Nome:{nome} - Telefone:{telefone} - Condição:{condicao}'

