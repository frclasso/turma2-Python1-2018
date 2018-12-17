#!/usr/bin/env python3

import vagas
import cadastroDeClientes
import controle_vagas_estacionamento
print()

# caso necessitem acessar as funcoes

# print(dir(vagas))
# print(dir(cadastroDeClientes))
# print(dir(controle_vagas_estacionamento))

menu = int(input( """
        ===================================
        Bem vindo ao estacionamento Central
        ===================================
        Digite 1 para iniciar novo dia(zerar vagas do dia anterior).
        Digite 2 entrada de cliente com cadastro.
        Digite 3 saida de veiculo cliente.
        Digite 4 para exibir vagas disponiveis.
        Digite 5 cadastro de novo cliente.
        Digite 0 para sair."""))
print()


try:
    if menu == 0:
        from PIL import Image, ImageFilter
        img = Image.open('f2019.jpg')
        img.show()
    elif menu == 1:
        vagas.zeraVagas()
    elif menu == 2:
        print(controle_vagas_estacionamento.entradaCliente())
    elif menu == 3:
        print(controle_vagas_estacionamento.saidaCliente())
    elif menu == 4:
        print(vagas.vagasDisponiveis)
    elif menu == 5:
        print(cadastroDeClientes.novoCliente())
    else:print('Opção incorreta, digite um número de 1 a 5.')
except ValueError:
    print('É preciso digitar um número inteiro') # erro




