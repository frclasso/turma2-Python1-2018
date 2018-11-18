#!/usr/bin/env python3

#revisao
d = {} # dicionario vazio
d['1'] = 'Um'

myDict = {'agua': 1, 'terra':2, 'fogo':3, 'ar':4}

# Acessando valores
print(myDict['agua'])
print(myDict['terra'])
print(myDict['fogo'])
print(myDict['ar'])
print()

# Usando um laço for

for x, y in myDict.items():
    print(x, '=>', y)
print()

# imprimindo um dionario de chaves e valores
print(myDict.items())
# apenas chaves
print(myDict.keys())
# apenas valores
print(myDict.values())
print()

# Atualizando valores
myDict['agua'] = 100  # modificando valores existentes
myDict['vento'] = 200 # inserindo novo
print(myDict)

# metodo update
student = {'Name':'John', 'Age':34, 'courses':['Math','Science']}
student.update({'Name':'Fabio', 'Phone':'9999-8888'})
print(student)

# Deletando
# metodo pop
#student.pop('Age')

# metodo __delitem__
#student.__delitem__('Phone')
# Metodo del
#del student['courses']
#print(student)

# metodo clear, deleta todo o conteudo docionario
# student.clear()
# print(student)

# Deletando o dicionario em si
#del student
#print(student) # Erro student Nont Defined

# Retornar valores
# metodo get, caso nao encontre a chave nao retorna Erro
print(student.get('phone'), ': Valor nao encontrado.')

# tamanho
print(len(student))

# str
print('{}'.format(str(myDict)))

