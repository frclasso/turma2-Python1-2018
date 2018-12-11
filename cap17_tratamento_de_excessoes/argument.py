def temp_converter(var):
    try:
        return int(var)
    except ValueError as Argument:
        print('O argumento nao contem numeros', Argument)



temp_converter(3.0)