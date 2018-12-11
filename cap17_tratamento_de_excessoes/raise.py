#!/usr/bin/env python3


def functionName(level):
    if level < 1:
        raise Exception(level)
    return level


try:
    l = functionName(-10)
    print('leve=', l)
except Exception as e:
    print('Erro in level argument', e.args[0])


