num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisivel por 2 e por 3")
    else:
        print("Divisivel por 2 mas nao por 3.")
else:
    if num % 3 == 0:
        print("Divisivel por 3 mas nao por 2.")
    else:
        print("Nao é divisivel por 3 nem por 2.")

print('Done.')