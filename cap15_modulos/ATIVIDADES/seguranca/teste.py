
import random
senha = []

numeros = ('0','1','2','3','4','5','6','7','8','9')
# for i in range(4):
#     n = random.choice(numeros)
#     senha.append(n)
# print(senha)

minusculas = ('abcdefghijklmnopqrstuvwxz')
maiusculas = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = range(10)
simbolos = ('!@#$%^&*')

hard_senha = []
for m in maiusculas:
    hard_senha.append(m)
    for a in minusculas:
        hard_senha.append(a)
        for n in num:
            hard_senha.append(n)
            for s in simbolos:
                hard_senha.append(s)

print(hard_senha)