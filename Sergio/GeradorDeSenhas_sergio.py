import random

def password():
    alfabeto = []
    for i in range(26):
        a = chr(i + 65)
        alfabeto.append(a)
    s1 = str(random.randint(00, 99))
    s2 = str(random.randint(100, 999))
    s3 = random.choice(alfabeto)
    s4 = random.choice(alfabeto)
    st = (s1+s3+s4+s2)
    return st

print(50* '=')
print('Gerador de Senhas'.center(50, '-'))
print('='*50)
print('''\nDigite abaixo o número de pessoas que deseja cadastrar,
fornecendo o nome de acesso, para o sistema criar uma senha.''')

usuarios = {}

time = int(input('\nInforme o número de pessoas:  '))

for a in range(1, time+1):
    name = input(f'Digite o nome da {a}º pessoa: ').upper()
    senha = password()
    usuarios[name] = senha
print('\nSegue abaixo os nomes com a senha de acesso ao sistema:')
for a, b in usuarios.items():
    print(f'{a:8} = {b}')

print('\nFim do cadastro!')
