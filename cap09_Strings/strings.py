str = 'Curso de Python 3'

# acessando valores
# indexando
# print(str)
# print(str[0])
# print(str[-1])

# fatiando/slice
# print(str[:]) # imprime tudo
# print(str[:8])
# print(str[6:8])


# Imutavel
str2 = str[:9] + 'Julia'
print(str2)
#
# # membership
if 'P' in str:
    print("ok")
else: print("Not ok")

# # tamamnho -  len()
print(len(str))

# loops

# for x in str:
#     print(x, end=' # ')

# for x, y in enumerate(str, start=1):
#     print(x, y)

# indice = 0
# while indice < len(str):
#     print(indice)
#     indice += 1


# find (str, ch)
palavra = 'engenharia na unisul, univali, estacio, ufsc'
#print(palavra.find('ria')) # imprime indice

#contar letras
contador  = 0
for l in palavra:
    if l == 'a':
        contador += 1
print(f"Quantidade de letras 'a': {contador}")

print("aula de python".upper())
print("AULA DE PYTHON".lower())
print("AULA DE PYTHON".title())
print("AULA DE PYTHON".capitalize())
print("AULA DE PYTHON".count('A'))
print("AULA DE PYTHON".split())
# lista = ['AULA', 'DE', 'PYTHON']
# lista.join()
#
# split()
# listaDePalavras = ("AULA DE PYTHON".split())
# print(len(listaDePalavras))


# strip()

string = "*** curso de Python da JCAVI treinamentos ***"
print(string.strip('*'))
print(string.lstrip('*'))
print(string.rstrip('*'))
print(string.replace('Python', 'Julia'))
string2 = 'PY'
print(string.index('Python'))
print(string[13])



# lista1 = [1,2,3,4,5]
# #lista2 = lista1
#
# lista2 = lista1[:]
#
# print(lista2)
# print(id(lista1))
# print(id(lista2))
# lista2[0]=1000
# print(lista2)
# print(lista1)
