import sys

lista = [1,2,3,4,5]
it = iter(lista)
#print(next(it))

# for x in lista:
#     print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


def soma(x, y):
    return (x + y)
