#!/usr/bin/env python3

# Sistema de login
# verificar usuario e senha

import admin

# funcao para verificar usuario
# Se usuario for root, poderes administrativos
# Do contrario, acesso limitado

user = admin.usuario # variavel de admin.py
key = admin.senha

# Entrada
usuario = input('Digite usuario')
senha = input('Digite senha: ')

# Verificacao de usuario
if usuario == user and senha == key:
    print('Voce é super usuario')
else:
    print('Voce é um usuario comum.')

#




# user = 'Admin'
# login = True  # esperementem alterar para False
#
# if user == 'Admin' and login:
#     print('Voce logou corretamente')
# else:
#     print('Bad Credentials')