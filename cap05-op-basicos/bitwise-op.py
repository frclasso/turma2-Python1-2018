a = 60 # 0011 1100
b = 13 # 0000 1101

print('a = ', a,':', bin(a), 'b = ',b,':',bin(b))
c = a & b # 12 = 0000 1100
print("Resultado de a AND b: ", c,':',bin(c))

c = a | b # 61 = 0011 1101
print("Resultado de a OR b: ", c,':',bin(c))

c = a ^ b # 49 = 0011 0001
print("Resultado de a XOR b: ", c,':',bin(c))

c = ~a # -61 1100 0011
print("Resultado complemento de a: ", c,':',bin(c))

c = a << 2 # 240 = 1111 0000
print("Resultado LEFT SHIFT: ", c,':',bin(c)[2:])

c = a >> 2 # 15  = 0000 1111
print("Resultado RIGHT SHIFT: ", c,':',bin(c)[2:])


