# _*_coding: utf-8 _*_

print('#*' * 15)
print('#'*7,  '\033[1;32mT A B U A D A\033[m',  '#'*7)
print('#*' * 15)

num = int(input('Digite um número inteiro para calcular a tabuada: '))
resp = 'S'
while resp == 'S':
    for n in range(1, 11):
        print(f'{num}  x {n:2} = {num*n:2}')
    print('#*' * 10)
    resp = str(input('\nQuer continuar (S/N)? ')).upper()
    if resp == 'S':
        num = int(input('Digite um número inteiro para calcular a tabuada: '))

print('Obrigado por utilizar o meu programa!.')
