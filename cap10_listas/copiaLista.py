from listas import cavaleiros, miscelania, elementos


def copiaLista(lista):
    novaLista = []
    novaLista = lista[:]  # ERRO
    return novaLista

# teste
# print(copiaLista(cavaleiros))
# copiaLista(elementos)