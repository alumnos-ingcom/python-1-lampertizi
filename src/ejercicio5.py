################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.

PRE: 2 n° enteros

POST: obtener el cociente y el resto
"""

def division_lenta(dividendo,divisor):
    """
    Calcula el cociente y resto entre 2 n° mediante restas sucesivas
    """
    count = dividendo
    cociente = 0
    
    while count > 1:
        if (count - divisor) < 0:
            temp = count
            count = count - divisor
        else:
            count = count - divisor
            cociente = cociente + 1
    
    verificador = cociente * divisor + abs(count)
    
    if verificador != dividendo:
        count = temp
    return cociente,count
    
def principal():
    """
    Ésta es la función que interactúa con el usuario
    """

    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    cociente,resto = division_lenta(dividendo,divisor)
    print(f"cociente = {cociente}\nresto = {resto}")

if __name__ == "__main__":
    principal()
