#!/usr/bin/env python3

"""variavel whisList é iniciada com uma lista vazia, que receberá seus elementos
a partir do input , salvando os valores."""

whishList = []
while True:
    coisas = input('Digite um nome de algo que voce goste, ou 0 para sair:')
    if coisas == '0':
        break
    else:
        whishList.append(coisas)
        print('Adicionado')

print()
print(f'Sua lista de desejos: {whishList}')
print(f'Quantidade de objetos: {len(whishList)}')