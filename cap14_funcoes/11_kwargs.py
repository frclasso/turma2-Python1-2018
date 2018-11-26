#!/usr/bin/env python3


def main():
    testFunc(5,6,7,8,9,10, one=1, two=2, tree=3, four=4)


def testFunc(this, that, other, *args, **kwargs):
    print()
    print("This is a test function",
          kwargs['one'], kwargs['two'], kwargs['tree'], kwargs['four'],
          this, that, other, args)
    print()


if __name__=="__main__":main()