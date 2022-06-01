################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero retorne
una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
PRE: 3 n° enteros

POST: los 3 n° ordenados
"""

def menor_a_mayor(val1,val2,val3):
    """
    Ordena 3 n° de menor a mayor
    """
    numbers = []
    if val1 is val2 and val1 < val3:
        numbers.append(val1)
        numbers.append(val2)
        numbers.append(val3)
    if val1 is val3 and val1 < val2:
        numbers.append(val1)
        numbers.append(val3)
        numbers.append(val2)
    if val2 is val3 and val2 < val1:
        numbers.append(val2)
        numbers.append(val3)
        numbers.append(val1)
    if val1 < val2 and val1 < val3:
        numbers.append(val1)
        if val2 < val3:
            numbers.append(val2)
            numbers.append(val3)
        else:
            numbers.append(val3)
            numbers.append(val2)
    elif val2 < val1 and val2 < val3:
        numbers.append(val2)
        if val1 < val3:
            numbers.append(val1)
            numbers.append(val3)
        else:
            numbers.append(val3)
            numbers.append(val1)
    elif val3 < val1 and val3 < val2:
        numbers.append(val3)
        if val2 < val1:
            numbers.append(val2)
            numbers.append(val1)
        else:
            numbers.append(val1)
            numbers.append(val2)
    return tuple(numbers)

def mayor_a_menor(val1,val2,val3):
    """
    Ordena 3 n° de mayor a menor
    """
    numbers = []
    if val1 > val2 and val1 > val3:
        numbers.append(val1)
        if val2 > val3:
            numbers.append(val2)
            numbers.append(val3)
        else:
            numbers.append(val3)
            numbers.append(val2)
    elif val2 > val1 and val2 >val3:
        numbers.append(val2)
        if val1 > val3:
            numbers.append(val1)
            numbers.append(val3)
        else:
            numbers.append(val3)
            numbers.append(val1)
    elif val3 > val1 and val3 > val2:
        numbers.append(val3)
        if val2 > val1:
            numbers.append(val2)
            numbers.append(val1)
        else:
            numbers.append(val1)
            numbers.append(val2)
    return tuple(numbers)

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    num1 = int(input("Ingrese el 1er n°: "))
    num2 = int(input("Ingrese el 2do n°: "))
    num3 = int(input("Ingrese el 3er n°: "))
    resultado = menor_a_mayor(num1,num2,num3)
    resultado2 = mayor_a_menor(num1,num2,num3)
    print(resultado)
    print(resultado2)

if __name__ == "__main__":
    principal()

