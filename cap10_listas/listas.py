elementos = ['agua','terra', 'fogo', 'ar']
cavaleiros = ['guerra','fome', 'peste', 'morte']
miscelania = []

# #add itens
# elementos.append('vento') # adiciona um item no final da lista
# elementos.insert(0, 'trovão') # adiciona conforme indice
#
miscelania.extend(elementos) # copia itens de uma lista para outra
#print(miscelania)
#
miscelania.extend(cavaleiros)
#print(miscelania)
#
# # Copiar itens
# novaLista = cavaleiros[:]
# print(novaLista)
#
# #del elementos
#
# elementos.pop() # deleta no final da lista
# print(elementos)
#
# elementos.remove('fogo') # deleta de acordo com nome
# print(elementos)
#
# del elementos[0] # deleta de acordo com indice
# print(elementos)
#
# # laços
# for e, c in enumerate(cavaleiros, start=1):
#     print(e,'==>',c)
#
#
# def contaElementos(lista): # com parametro
#     i = 0
#     while i < len(lista): # valor acompanha o tamanho da lista
#         print(lista[i])
#         i += 1
#     print("Again...")

# print("Elementos")
# contaElementos(elementos)
# print("Cavaleiros")
# contaElementos(cavaleiros)
# print("Miscelania")
# contaElementos(miscelania)
