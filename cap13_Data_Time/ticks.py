#!/usr/bin/env python3

import time

ticks = time.time()
#print('Numbers of ticks since 12:00am, January 1, 1970:', ticks)

#print(time.localtime())
print(f'Ano:{time.localtime()[0]}')
print(f'Mes:{time.localtime()[1]}')
print(f'Dia:{time.localtime()[2]}')
print(f'Hora atual:{time.localtime()[3]} min:{time.localtime()[4]}')
print(f'Minuto:{time.localtime()[4]}')
print(f'Segundos:{time.localtime()[5]}')