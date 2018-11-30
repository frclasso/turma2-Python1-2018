#!/usr/bin/env python3

# Sistema de login
# verificar usuario e senha
# funcao para verificar usuario
# Se usuario for root, poderes administrativos
# Do contrario, acesso limitado

import myadmin


print('Modulo login importado com sucesso')


user = myadmin.usuario # variavel de myadmin.py
key = myadmin.senha


def superAdmin():
    usuario = input('Digite o nome de usuario:')
    senha = input('Digite sua senha:')
    if usuario == user and senha == key:
        print('Voce é um usuario com super poderes')
        print('Cadastrar novo usuario?')
        # importar cadastroUsuario.py > novoCadastro()
        # importar gerador_de_senhas > geraSenha()
    else:
        print('Usuario nao autorizado')


def regularUser():
    usuario = input('Digite o nome de usuario:')
    senha = input('Digite sua senha:')
    print('Bem vindo:', usuario)


def main():
    print("Selecione uma opcao - super para ADMIN ou regular para usuarios comuns ")
    login = input('super x regular:')
    if login == 'super':
        superAdmin()
    elif login == 'regular':
        regularUser()
    else:
        print("Ops, voce precisa escolher entre super ou regular")


if __name__=="__main__":main()
