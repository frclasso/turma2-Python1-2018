
# ela nao retorna caso nao encontra a chave
pessoa = {'Name':'Zara'}
print('Value : {}'.format(pessoa.setdefault('Age', None)))
print('Value : {}'.format(pessoa.setdefault('Sex', 'Female')))
print(pessoa)


