#!/usr/bin/env python3

def main():
    inFile = open('berlim.jpg', 'rb') #rb, read binary
    outFile = open('berlim_copy.jpg', 'wb')
    while True:
        buf = inFile.read(1024)
        if buf:
            outFile.write(buf)
            print('.', end='', flush=True)
        else:break
    outFile.close()
    print('\nDone...')

if __name__=="__main__":main()