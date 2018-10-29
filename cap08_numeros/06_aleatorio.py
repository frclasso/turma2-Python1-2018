import random

elementos = ['agua', 'ar', 'terra', 'fogo']
num = [1,2,3,4,5,6,7,8]

# choice(seq)
print(random.choice(elementos))
print(random.choice('Welcome home boy'))
print(f"Choice: {random.choice(num)}")


# random sample
megaSena = random.sample(range(61), 6) # range de 0 a 60, gerando 6 numeros
print(f"Mega sena do milhao: {megaSena}")
print()



# randgange (start, stop, step)
print(f"RandRange: {random.randrange(0, 100, 5)}")

# random.random(0.0, 1.0)
print(random.random())

# seed()
# random.seed()
# print("Random number with default seed: ", random.random())
#
# random.seed(1)
# print("Random number with int seed: ", random.random())
#
# random.seed("hello")
# print("Random number with string seed: ", random.random())

# shuffle - nao funciona com tupla

random.shuffle(elementos)
print(elementos)

random.shuffle(num)
print(num)

# Uniform
print(f"Random uniform float(50, 100): {random.uniform(50,100)}")

print(round(random.uniform(50,1000), 3))
print()
# # itertools.combinations
import itertools
colors = ["Vermelho", "Azul", "Roxo", "Laranja", "Amarelo", "Lilás"]
contador = 0
for c in itertools.combinations(colors, 4): # 3 elements
    contador += 1
    print(c)
print(contador)
#
# itertools.permutations
election = {1:'Pedro', 2:'Giovanna', 3:'Erick'}
for p in itertools.permutations(election):
    print(p)
