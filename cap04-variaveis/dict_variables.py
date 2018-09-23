dict = {}

dict['one'] = 'Numero 1'
dict['2'] = 'Numero 2'
dict['tres'] = 'Numero 3'

dict2 = {'Name':'John', 'code':6734, 'department':'Sales'}

print(dict['one'])
print(dict['2'])
print(dict.items())
print(dict.keys())
print(dict.values())

print()
print(dict2)
print(dict2.items())
print(dict2.keys())
print(dict2.values())
print('Funcionario {} codigo {},'
      ' departamento {}'.format(dict2['Name'],
        dict2['code'],dict2['department']))
