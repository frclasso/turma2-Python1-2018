#!/usr/bin/env python3

# Variaveis locais x globais

money = 200

def addMoney():
    global money
    money = money + 1

print(money)

addMoney()
print(money)

