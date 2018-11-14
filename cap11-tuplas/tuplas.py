tup3 = 'a', 'b', 'c', 'd'
print(tup3)

tupUm = 1,
print(tupUm)

# index
print(tup3[0])
# Fatiar
print(tup3[2:])
# copiar elementos
tup4 = tup3[:1]
print(tup4)

# concatenar
t5 = tup3 + tupUm
print(t5)
# del t5
# print(t5)
print(tup3)
print(len(tup3))

# repetir
double = (tup3 * 2)

#contar elementos
double.count('a')

# Verificar se eh membro de
print('a' in tup3) # retorna True caso encontre
print('Python' not in tup3)

# Itera
for x, v in enumerate(tup3, start=1):
    print(x,'==>',v)

numeros = (300, 45, 25, 1000, 3, 5,4)
print(max(numeros)) # verifica o valor maximo em uma sequencia
print(min(numeros))# verifica o valor minimo em uma sequencia

# Metodo tuple, converte uma sequencia em tupla

s = 'Python'
print(tuple(s))

lista = [1,2,3,4,5]
print(tuple(lista))

x = {1,2,4,4,4,7,3,5,6,78,}
print(tuple(x))
