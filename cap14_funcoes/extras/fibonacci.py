def fibo(n):
    "Print a Fibonacci series up to n"
    a,b = 0,1
    while a < n:
        print(a, end=' ', flush=True)  # limpa memoria
        a,b = b, a + b  # Sequencia Fibonacci
    print()

print(fibo(6))

# salvar numa lista
def fibo2(n):
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fibo2(6))

