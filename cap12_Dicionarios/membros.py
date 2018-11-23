contatos = {'Fabio':'999-8888',
            'Renato':'999-7777',
            'Amanda':'999-1111',
            'Nicolas':'999-6666',
            'Marcelo':'999-5555',
            'Matheus':'999-4444',
            'Julio':'999-3333',
            'Marcelo Gevaerd':'999-2222'}


print('Amanda' in contatos)
print('Joao' in contatos)  # False
print('Joao' not in contatos) # True

print('999-8888' in contatos) # False
print('999-8888' in contatos.values()) # True
