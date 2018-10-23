

# menu de opcoes

voto = input("Digite seu voto: ")

# lista de confirmacao
confirma = ['C', 'c', 'S', 's', 'sim', 'confirma', 'CONFIRMA']

voto17 = 0
voto13 = 0
votoBranco = 0
votoNulo = 0
votosInvalidos = 0
# Menu de opcoes:


# while True:
#     voto = input("Digite seu voto: ")
#     if voto == '0':
#         print('Saindo...')
#         break
#     elif voto == '13':
#         confirmacao = input("Confirma?")
#         if confirmacao in confirma:
#             voto13 += 1 # voto = voto + 1
#         else:
#             voto13 = voto13
#             print("Voto confirmado")
#     # elif voto == '17':
#     #     # confirmacao input, caso esteja em (in) confirma, incrementa
#     #     confirmacao = input("CONFIRMA SEU VOTO?")
#     #     if confirmacao in confirma:
#     #         voto17 += 1 # voto = voto + 1
#     #     else:
#     #         voto17 = voto17
#     #         print("Vonto confirmado")
#     # elif voto == '':
#     #     # confirmacao input, caso esteja em (in) confirma, incrementa
#     #     confirmacao = input("CONFIRMA SEU VOTO?")
#     #     if confirmacao in confirma:
#     #         votoBranco += 1 # voto = voto + 1
#     #     else:
#     #         votoBranco = votoBranco
#     #         print("Vonto confirmado")
#     else:
#         print("Voto Nulo")
#         # confirmacao input, caso esteja em (in) confirma, incrementa
#         confirmacao = input("CONFIRMA SEU VOTO?")
#         if confirmacao in confirma:
#             votoNulo += 1 # voto = voto + 1
#         else:
#             votoNulo = votoNulo
#             print("Vonto confirmado")
#
# print('/'*20 + 'TOTAL DE VOTOS APURADOS' + '/'*20)
# print(f'Votos em Branco: {votoBranco}')
# print(f'Votos Nulos: {votoNulo}')
# print(f"Total de votos inválidos: {votoBranco + votoNulo}")
# print(f'Votos para Haddad: {voto13}')
# print(f'Votos para Bolsonaro: {voto17}')
# print(f"Total de votos válidos: {voto17 + voto13}")