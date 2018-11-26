#!/usr/bin/env python3

# usando a palavra *args


def palavras(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Sem parametros pre-dfinidos')

def main():
    x = ('Florianopolis', 'Python', 'Brasil', 'Go', 'Django')
    palavras(*x) # Chamada da funcao


if __name__=="__main__":
    main()