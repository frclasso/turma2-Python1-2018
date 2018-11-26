#!/usr/bin/env python3


def main():
    testFunc(1,2,3,41,42,43)


def testFunc(this, that, other, *args):
    print(this, that, other)
    for n in args:
        print(n, end=',')


if __name__=="__main__":main()