from listas import cavaleiros,miscelania, elementos


def contaElementos(lista): # com parametro
    i = 0
    while i < len(lista): # valor acompanha o tamanho da lista
        print(lista[i])
        i += 1
    print("Done...")
    print(f"Quantidade de elementos na lista: {len(lista)}")

# teste
# contaElementos(cavaleiros)