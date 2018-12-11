#!/usr/bin/env python3

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'Expected at least 1 argument. got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError((f'Expected at most 3 argument. got {numargs}'))

    # generator
    i = start
    while i <= stop:
        yield i
        i+= step


def main():
    try:
        for i in inclusive_range(1, 100, 5):
            print(i, end=", ")
        print()
    except TypeError as e:
        print(f'Range error', e)


if __name__=="__main__":main()
