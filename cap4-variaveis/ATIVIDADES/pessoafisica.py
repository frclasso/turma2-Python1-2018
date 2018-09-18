#!/usr/bin/env python3

"""Desenvolver uma aplicação para cadastro de pessoa física
"""



nome = 'Fabio Classo'
idade = 43
cpf = '047.444.667.888/44'
rg = '622.333.44'
telefone = '(48)99174-3152'
endereco = "Rua Caminhos dos Açores 1600, Sto Antonio de Lisboa - Florianopolis - SC"

empresa = "Sativa Life Technologies"
cnpj = '000.111.222.333/10'
ramo = 'Tecnologia'


#print('Nome:', nome,'\nMinha idade:', idade,'\CFP:',cpf)


dadosPessoais = nome + '\n'+ str(idade) + '\n' +cpf +'\n' +rg +'\n'+telefone+'\n'+endereco

#dadosProfissionais = empresa + cnpj + ramo

print(dadosPessoais)