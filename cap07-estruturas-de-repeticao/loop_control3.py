def main():
    s = "This is a string"
    i = 0
    while i < len(s):
        if s[i] == 's':
            continue # Mais uma naba
        print(s[i], end='')
        i += 1
    else:
        print(' ,done.')


main()