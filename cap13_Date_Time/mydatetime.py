from datetime import datetime


now = datetime.now()

print(f'Now: {now}') # data completa
print(f'Date: {now.date()}') # data ano-mes-dia
print(f'Year: {now.year}') # ano
print(f'Month: {now.month}') # mes (numerico)
print(f'Day:{now.day}') # dia (numerio)
print(f'Hour: {now.hour}') # hora
print(f'Minute: {now.minute}') # minuto
print(f'Seconds:{now.second}') # segundo

print(f'Time: {now.time()}') # hora:minuto:segundo
