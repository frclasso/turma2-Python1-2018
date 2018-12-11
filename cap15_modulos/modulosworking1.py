#!/usr/bin/env python3


import sys

def main():
    #Python version
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    print()

    # Funcoes do OS
    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    print()


if __name__=="__main__":main()