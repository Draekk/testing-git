# def recorrer_posiciones(cont1, pos, objetos, sentido = False):
#     if pos == 5:
#         sentido = True
#     elif pos == 0:
#         sentido = False
    
#     if not sentido:
#         objetos[pos] = cont1
#         print(objetos)
#         objetos[pos] = 0
#         recorrer_posiciones(cont1, pos + 1, objetos, sentido)
#     else:
#         objetos[pos - 1] = cont1
#         print(objetos)
#         objetos[pos - 1] = 0
#         recorrer_posiciones(cont1, pos - 1, objetos, sentido)

# box = [0,0,0,0,0]
# recorrer_posiciones(1,0,box)




def generar_combinaciones_clave(digitos_disponibles, clave_actual=[]):
    # Caso base: si la clave_actual contiene 5 dígitos, hemos encontrado una combinación
    if len(clave_actual) == 5:
        return 1

    # Inicializar el contador de combinaciones
    combinaciones = 0

    # Iterar sobre los dígitos disponibles y generar las combinaciones recursivamente
    for digito in digitos_disponibles:
        # Si el dígito ya está en la clave_actual, saltar a la siguiente iteración
        if digito in clave_actual:
            continue

        # Agregar el dígito a la clave_actual y generar las combinaciones recursivamente
        combinaciones += generar_combinaciones_clave(digitos_disponibles, clave_actual + [digito])

    return combinaciones

# Dígitos disponibles del 1 al 5
digitos_disponibles = [1, 2, 3, 4, 5]

# Calcular el número de combinaciones posibles
total_combinaciones = generar_combinaciones_clave(digitos_disponibles)

print("El número total de combinaciones posibles de claves en el cajero es:", total_combinaciones)

