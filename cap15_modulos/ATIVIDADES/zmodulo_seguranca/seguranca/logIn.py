#!/usr/bin/env python3

# Sistema de login
# verificar usuario e senha
# funcao para verificar usuario
# Se usuario for root, poderes administrativos
# Do contrario, acesso limitado

import myadmin

user = myadmin.usuario # variavel de myadmin.py
key = myadmin.senha

# Entrada
usuario = input('Digite usuario: ')
senha = input('Digite senha: ')

# Verificacao de usuario
if usuario == user and senha == key:
    print('Voce é super usuario')
else:
    print('Voce é um usuario comum.')
