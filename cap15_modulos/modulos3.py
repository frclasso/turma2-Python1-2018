import datetime


def main():

    now = datetime.datetime.now()
    print(now)
    print()
    print(f'Ano:{now.year}')
    print(f'Mes:{now.month}')
    print(f'Dia:{now.day}')
    print(f'Hora:{now.hour}')
    print(f'Minute:{now.minute}')
    print(f'Segundo:{now.second}')
    print()
    print(f'Calendar{now.year}/{now.month}/{now.day}')
    print(f'Clock {now.hour}:{now.minute}:{now.second}')


if __name__=="__main__":main()