""" metodo fromkeys()
retorna um novo dicionário cujas chaves são os elementos de uma sequencia e cujos
valores são todos iguais ao argumento valor.
   Sintaxe: dict.fromkeys(seq[, value])
"""

seq = ['name','age', 'sex']
dict = dict.fromkeys(seq, 'NULL') # caso nao passe valores = None
print('Novo dicionario:{}'.format(str(dict)))

print(dict.fromkeys(['Joao', 'Maria'], 0))