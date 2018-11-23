
# copiando
myDict = {'agua': 1, 'terra':2, 'fogo':3, 'ar':4}
newDict = myDict.copy()
print(newDict)

# Aliasing vs copyng

alias = myDict # aplelido
alias['vento'] = 200
print(alias)
print(myDict)

