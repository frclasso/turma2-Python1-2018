def main():
    s = 'This is a string'
    for c in s:
        if c == 's':
            #break
            continue
        print(c, end='')

main()