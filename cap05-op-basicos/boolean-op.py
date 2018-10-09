a = True
b = False

if a and b:
    print('Expressao eh verdadeira')
else:
    print('Expressao nao e verdadeira')

if not b:
    print("verdadeiro")
else:
    print('false')

x = ('bear', 'bunny', 'tree', 'sky', 'rain')
y = 'bear'

if y in x:
    print('Expressao verdadeira')
else:
    print('Expressao falsa')

if y is not x[0]:print('Expressao verdadeira:', y)
else:print("Expressao falsa",y)

