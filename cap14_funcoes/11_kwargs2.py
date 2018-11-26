#!/usr/bin/env python3


def main():
    x = dict(SC='Greve', SP='Paralisacao', RJ='Corrupcao', PR='Lava jato')
    People(**x)


def People(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('O povo de {} diz: {}.'.format(k, kwargs[k]))
    else:print('Sem parametros')


if __name__=="__main__":main()