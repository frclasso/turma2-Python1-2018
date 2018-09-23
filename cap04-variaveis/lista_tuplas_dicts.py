
print("Listas______")
minhaLista = ['abcd', 2.22, 'efgh', 'Python']
print(minhaLista[0])
print(minhaLista[-1])
print(minhaLista[-2])
# Adicionando elementos ao final da lista
minhaLista.append('Fogo')
print(minhaLista)
minhaLista.insert(5, 'Terra') # passar a posicao
print(minhaLista)
minhaLista.insert(0, 'agua') # passar a posicao
print(minhaLista)
del minhaLista[-1] # passar a posicao
print(minhaLista)
del minhaLista[:] # deletando todos os elementos
print(minhaLista)
del(minhaLista) # deletando a lista em si
#print(minhaLista)

print("Tuplas______")
minhaTupla = ('abcd', 2.22, 'efgh', 'Python', [1,2,3])
print(minhaTupla)
print(minhaTupla[0])
print(minhaTupla[-1])
print(minhaTupla[-2])
print(minhaTupla[:2])
# del minhaTupla[0] # TypeError: 'tuple' object doesn't support item deletion
# minhaTupla.append('Fogo') #AttributeError: 'tuple' object has no attribute 'append'
# minhaTupla.insert(5, 'Terra') #AttributeError: 'tuple' object has no attribute 'insert'
print(minhaTupla[4])
print("Dicionarios______")
pessoa = {'Nome':'fabio',
          'identidade':'9000000',
          'idade':18,
          'telefone':999988888
}
print(pessoa['Nome'])
print(pessoa['identidade'])

del pessoa['identidade']
print(pessoa)
pessoa['cpf'] = '444.333.222.111/00'
print(pessoa)

#pessoa['Nome'] = 'Fabio'
pessoa.update({'Nome':'Fabio'})
print(pessoa)
pessoa.clear() # deleta todos os elementos
print(pessoa)

del(pessoa) # deleta o dicionario
#print(pessoa)