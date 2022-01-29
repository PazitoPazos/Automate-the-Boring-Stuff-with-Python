def commacode(lista):
    for i in lista:
        if i == lista[0]:
            print('\'' + str(i) + ', ',end="")
        elif i == lista[-2]:
            print(str(i) + ' and ',end="")
        elif i == lista[-1]:
            print(str(i) + '\'')
        else:
            print(str(i) + ', ',end="")