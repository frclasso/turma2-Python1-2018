from listas import cavaleiros, miscelania, elementos


def delFinal(lista):
    deletado = lista.pop()
    print(f"Item deletado: {deletado}")
    print(f"Nova lista:{lista}")

#teste
#delFinal(elementos)