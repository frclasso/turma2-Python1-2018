#!/usr/bin/env python3

"""Aqui vamos  integrar o pesssoafisica1 e 2 em uma só aplicação
 de cadastro de pessoa física
"""
# Primeiro criamos um dicionario vazio para receber os dados
cadastroPessoaFisisca = {"Nome": None,
                         "Idade": None,
                         'CPF':None,
                         'RG':None,
                         'Telefone':None,
                         'Endereco':None,
                         'Empresa':None,
                         'CNPJ':None,
                         'Segmento':None}

"""Inserindo dados dinamicamente, observem que aqui usei as chaves dos nomes,
do dicionario em letras maiusculas e o nome das variaveis com letras
minusculas(caixa baixa) pra evitar confusão"""

nome = input('Digite seu nome: ')
idade = input('Sua idade: ')
cpf = input('Digite seu CPF: ')
rg = input('Digite seu RG: ')
telefone = input('Digite seu telefone: ')
endereco = input("Digite seu endereco: ")
empresa = input("Digite o nome da sua empresa: ")
cnpj = input("Digite o cnpj: ")
segmento = input("Qual a area de atuação de sua empresa?")

# Inserindo dados no dicionario
cadastroPessoaFisisca['Nome'] = nome
cadastroPessoaFisisca['Idade'] = idade
cadastroPessoaFisisca['CPF'] = cpf
cadastroPessoaFisisca['RG'] = rg
cadastroPessoaFisisca['Telefone'] = telefone
cadastroPessoaFisisca['Endereco'] = endereco
cadastroPessoaFisisca['Empresa'] = empresa
cadastroPessoaFisisca['CNPJ'] = cnpj
cadastroPessoaFisisca['Segmento'] = segmento

print('*' * 100)
print('*'* 50, "Dados Pessoais", '*'* 50)
print(f"Nome:{cadastroPessoaFisisca['Nome']}"
      f"\nIdade:{cadastroPessoaFisisca['Idade']}"
      f"\nCPF:{cadastroPessoaFisisca['CPF']} \nRG:{cadastroPessoaFisisca['RG']}"
      f"\nTelefone celular:{cadastroPessoaFisisca['Telefone']}"
      f" \nEndereço:{cadastroPessoaFisisca['Endereco']}")

print('*' * 100)
print('*'* 50, "Dados Profissionais", '*'* 50)
print(f"Nome da Empresa:{cadastroPessoaFisisca['Empresa']}"
      f"\nCNPJ:{cadastroPessoaFisisca['CNPJ']}"
      f"\nSegmento:{cadastroPessoaFisisca['Segmento']}")

print('*' * 100)
print('Done.')