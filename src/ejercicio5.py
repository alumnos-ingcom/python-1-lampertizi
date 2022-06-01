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
    assert divisor != 0, "no se puede dividir por cero jefe"
    count = abs(dividendo)
    cociente = 0
    while count >= 1:
        count = count - abs(divisor)
        cociente = cociente + 1
    if count < 0:
        cociente = cociente + 1
        cociente = cociente + count
        count = abs(count) + 1
    if dividendo < 0 or divisor < 0:
        verificador = cociente * abs(divisor) + count
        if verificador == abs(dividendo):
            return (-cociente,count)
    return(cociente,count)
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
