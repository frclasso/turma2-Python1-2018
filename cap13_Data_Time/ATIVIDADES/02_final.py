import os
import time
import sys
from datetime import datetime


def sleeping():
    x = 0
    while x < 5:
        print()
        print('Coletando informações...')
        print()
        # Usuarios e grupos
        print("Exibindo informações de usuário e grupos")
        print(f"Effective user: {os.geteuid()}")
        print(f"Effective group: {os.getegid()}")
        print(f"Actual User: {os.getuid()} {os.getlogin()}")
        print(f"Actual group: {os.getgid()}")
        print(f"Actual groups: {os.getgroups()}")
        print()

        # informações do sistema operacional
        print("Exbibindo informações do sistema operacional...")
        os.system('date; (sleep 3; date) &')

        v = sys.version_info
        print('Python version {}.{}.{}'.format(*v))

        w = (sys.platform).capitalize()
        print(f"Plataforma: {w}")

        z = (os.name).capitalize()
        print(f"OS name: {z}")
        print()

        print('Próxima atualização em 10 segundos')
        time.sleep(7)
        x += 1
        print()


sleeping()
print('*** Programa encerrado automaticamente ***')
now = datetime.now()
print()
print(f"<<< Ultima atualizacaoem >>> {now.date()} {now.hour}:{now.minute}")