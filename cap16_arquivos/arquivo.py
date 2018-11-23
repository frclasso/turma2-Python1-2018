#!/usr/bin/env python3

from datetime import datetime
import os, sys

now = datetime.now()
#
# print(f'Now: {now}') # data completa
# print(f'Date: {now.date()}') # data ano-mes-dia

modificadoEm = now

f = open('arquivo.txt', 'w')  # cria arquivo.txt e abre em modo write/escrita


v = sys.version_info
w = (sys.platform).capitalize()
z = (os.name).capitalize()
d = os.getcwd()
envDict = dict(os.environ)
# print(envDict)
# print(envDict['PATH'])
pyPath = envDict['PYTHONPATH']
shellPath = envDict['SHELL']
userLogin = envDict['LOGNAME']
homeDir = envDict['HOME']
pwd = envDict['PWD']

f.write('*'* 72)
f.write('\n\t\t\t\tObtendo informações do OS\n')
f.write('*'* 72)
f.write('\n')
f.write('\nPython version {}.{}.{}'.format(*v))
f.write(f'\nPYTHONPATH:{pyPath}')
f.write(f'\nSHELLPATH:{shellPath}')
f.write(f'\nLogin:{userLogin}')
f.write(f'\nHOME:{homeDir}')
f.write(f'\nDiretorio atual:{pwd}')
f.write(f'\nPlatform:{w}')
f.write(f'\nOS:{z}')
f.write(f'\nDiretório atual: {d}\n')
f.write('\n')
f.write('*'* 72)
f.write(f'\nHora da ultima modificacao: {modificadoEm}.\n')
f.write('*'* 72)
print('Done')

