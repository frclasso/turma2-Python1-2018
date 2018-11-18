#!/usr/bin/env python3

secret = 'swordfish'
pw = ''
auth = False      #autorizado inicia com valor false
count = 0         #contador de tentativas
max_attempt = 5   #numero maximo de tentativas


while pw != secret:  #enquanto condicao for verdadeira continua rodando
    count += 1
    if count > max_attempt: break  #se qtd de tentativas > maxima permitida (break)
    pw = input("{} : What's the secret word? ".format(count))
else:
    auth = True #autorizado muda de False para True
print('Authorized' if auth else 'Calling the FBI!')