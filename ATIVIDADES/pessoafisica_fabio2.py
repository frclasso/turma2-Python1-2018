#!/usr/bin/env python3

"""Desenvolver uma aplicação  (DICIONARIO) para
 cadastro de pessoa física
"""

nome = input('Digite seu nome: ')
idade = input('Sua idade: ')
cpf = input('Digite seu CPF: ')
rg = input('Digite seu RG: ')
telefone = input('Digite seu telefone: ')
endereco = input("Digite seu endereco: ")
empresa = input("Digite o nome da sua empresa: ")
cnpj = input("Digite o cnpj: ")
segmento = input("Qual a area de atuação de sua empresa?")

print(f"Ola {nome}, bom dia! Voce trabalha na {empresa}\n"
      f" seus dados estao corretos? cpf: {cpf},\n"
      f"identidade: {rg} e telefone:{telefone} ")