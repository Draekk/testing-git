def recursivity(clave : list, digit : int, cont : int = 0):
    exist = False
    long = len(clave)

    for i in clave:
        if i == digit:
            exist = True
            break
    if not exist:
        clave.append(digit)
    if long < 4:
        recursivity(clave, digit + 1, cont)
    else:
        print(clave)
        cont += 1
        if cont <= 5:
            clave = [cont + 1]
        else:
            clave
        digit = 0
        recursivity(clave, digit + 1, cont)
    if cont == 5:
        return


recursivity([], 1 )