
# Argumentos padrao

def printinfo(name='Fabio', age=40):
    """Imprime informacoes de usuario passadas como argumento de funcao"""
    print("Name:", name)
    print('Age:', age)
    return


# Chamando a funcao
printinfo() # Esqueceu de passar argumentos
printinfo(age=43) # Passou apenas um argumento
printinfo(age=43, name='Pedro') # Alterou a ordem dos argumentos
printinfo('Juliana', 40)
