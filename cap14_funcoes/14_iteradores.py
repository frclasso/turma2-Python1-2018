#!/usr/bin/env python3

lista = [1,2,3,4,5,6,7]

it = iter(lista)

print(next(it))
print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # Raise stop Iteration

for x in it:
    print(x, end=' ')