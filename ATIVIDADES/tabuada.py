#!/usr/bin/env python3

"""Desenvolver uma tabuada para ensino infantil."""
operacao =input("entre com a operacao matematica")
if operacao == '+':
    soma = x + y

tabuada = int(input("Entre valor da tabuda"))
# print(tabuada * 1)
# print(tabuada * 2)
# print(tabuada * 3)
# print(tabuada * 4)
# print(tabuada * 5)
# print(tabuada * 5)
# print(tabuada * 2)
# print(tabuada * 2)

for x in range(1,10):
    print(f"Tabuada de: ",x * tabuada)
