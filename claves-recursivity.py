def recorrer_posiciones(digit, cont, pos, objetos, sentido = False):
    if pos == 5:
        print(f'clave: {objetos}, cont: {cont}')
        pos = 0
        cont += 1
    
    exist = False
    if not sentido:
        for i in objetos:
            if i == digit:
                exist = True
        if not exist:
            objetos[pos] = digit
        print(objetos)
        recorrer_posiciones(digit + 1, pos + 1, objetos, sentido)
    else:
        objetos[pos - 1] = digit
        print(objetos)
        objetos[pos - 1] = 0
        recorrer_posiciones(digit, pos - 1, objetos, sentido)

recorrer_posiciones(1, 0, [0,0,0,0,0])