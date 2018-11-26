# #!/usr/bin/env python3
#

def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step

def main():
    print('Essa e a funcao')
    for i in inclusive_range(0,25,5):
        print(i, end=', ')


if __name__=="__main__":main()


#print(list(range(25)))