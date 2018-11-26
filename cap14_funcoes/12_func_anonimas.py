#!/usr/bin/env python3

sum = lambda arg1, arg2:arg1 + arg2

#Chamada de funcao
print('Soma:', sum(10,20))
print('Soma:', sum(100,200))
print('Soma:', sum(1000,2000))

sub = lambda x,y: x - y
print("Subtracao:", sub(20, 10))
print("Subtracao:", sub(2020, 1010))
print("Subtracao:", sub(201, 101))

def calcula():
    soma = lambda x,y:x+y
    subatra = lambda x,y: x - y
    return soma(10,20), subatra(10,20), sum(10,10)

print(calcula())