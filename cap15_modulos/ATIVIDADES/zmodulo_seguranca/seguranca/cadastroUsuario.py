#!/usr/bin/env python3

### Modulo de cadastro de usuario

# So root pode cadastrar novos usuarios

print('Modulo cadastro usuarios importado com sucesso')

usuarios = ('root')
novosUsuarios = {'nome':None, 'senha':None}


def novoCadastro():
    user = input('Insira novo usuario: ')
    key = input('Insira nova senha:')
    novosUsuarios.update({'nome':user, 'senha':key})
    print('Usuario cadastrado com sucesso')


#print(novosUsuarios)

def imprimeUsuarios():
    pass

def deletaUsuarios():
    pass

def exportaUsuarios():
    pass