#!/usr/bin/env python3

"""Programa das eleicoes do TSE/JCAVI"""

print("""Eleições 2018 - 2nd turno
         Escolha o candidato de sua preferência
         0 (zero) para sair;
         13 para Haddad/Manuela;
         17 para Bolsonaro/Gen Mourão;
         Após escolher seu candidato pressione CONFIRMA(C/c/S/s)
         CONFIRMAR sem escolher = VOTO EM BRANCO
         Qualquer outro valor será NULO""")

print()
confirma = ['C','c','S','s']

# Contadores, variaveis inicializadas em 0 para contar os valores de entrada
votosEmBranco = 0
votos13 = 0
votos17 = 0
votosNulos = 0

while True:
    voto = input('Digite aqui seu voto: ')
    if voto == '0':
        print('Sair')
        break
    elif voto == '13':
        print('Haddad/Manuela')
        confirmacao = input('CONFIRMA(C/c/S/s)')
        if confirmacao in confirma:
            votos13 += 1
            print('VOTO CONFIRMADO')
        else:
            votos13 = votos13
            print('Voce nao CONFIRMOU seu voto')
    elif voto == '17':
        print('Bolsonaro/Gen Mourão')
        confirmacao = input('CONFIRMA(C/c/S/s)?')
        if confirmacao in confirma:
            votos17 += 1
            print('VOTO CONFIRMADO')
        else:
            votos17 = votos17
            print('Voce nao CONFIRMOU seu voto')
    elif voto == '':
        print('Voto em BRANCO')
        confirmacao = input('CONFIRMA(C/c/S/s)?')
        if confirmacao in confirma:
            votosEmBranco += 1
            print('VOTO CONFIRMADO')
        else:
            votosEmBranco = votosEmBranco
            print('Voce nao CONFIRMOU seu voto')
    else:
        print('Voto NULO')
        confirmacao = input('CONFIRMA(C/c/S/s)?')
        if confirmacao in confirma:
            votosNulos += 1
            print('VOTO CONFIRMADO')
        else:
            votosNulos = votosNulos
            print('Voce nao CONFIRMOU seu voto')


print('/'*20 + 'TOTAL DE VOTOS APURADOS' + '/'*20)
print(f'Votos em Branco: {votosEmBranco}')
print(f'Votos Nulos: {votosNulos}')
print(f"Total de votos inválidos: {votosEmBranco + votosNulos}")
print(f'Votos para Haddad: {votos13}')
print(f'Votos para Bolsonaro: {votos17}')
print(f"Total de votos válidos: {votos17 + votos13}")