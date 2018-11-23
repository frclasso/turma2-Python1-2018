elementos = ['agua','terra', 'fogo', 'ar', ['guerra','fome', 'peste', 'morte']]

#print(elementos[4])
elementos[4][0] = 'war'
#print(elementos[4])

#criar
l = []

# Adicionar elementos

# Indexar
#l[0] = 1

# Fatiar
#l[:]

# Matrizes

matrix = [[1,2,3], [4,5,6], [7,8,9]]

# split

import string
poesia = 'O orvalho no carvalho'
print(poesia.split())

lista = ('O', 'orvalho', 'no', 'carvalho')
s = ' '
print(s.join(lista))

str = list('Python')
print(str)


num = [1,2,3,3,3,3,3,3,4,5,6]
num2 = [2000,3000]
# reverse
# num.reverse()
# print(num)
# append
num.append(7) # adiciona no final
num.insert(0, 1000)
num.extend(num2)
#print(num)

print(num.count(3))  # quantas vezes aparece
print(num.index(1000))
print(num[0])

# Deletar
#print(num)
#deletado = num.pop() # indicar o indice ou deletar o ultimo
#print(deletado)

num.remove(2000) # chave
print(num)
num.__delitem__(0)  # indice
print(num)

# Ordenar lista
lista = [8,6,3,6,8,3,1,4,9]
#lista.sort(reverse=True)
#print(sorted(lista))
