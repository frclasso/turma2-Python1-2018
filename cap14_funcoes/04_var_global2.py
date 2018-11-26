def calcula_tempo(velocidade, distancia):
    tempo = distancia/velocidade
    velocidade = 0
    return tempo


def calcula_distancia(velocidade, tempo):
    distancia = velocidade * tempo
    return distancia

v = 100 #  VARIAVEL GLOBAL

t = calcula_tempo(v, 5)
print(v)  # 100
print(t)

d = calcula_distancia(v, t)  # REUSO DE CODIGO
print(d)


