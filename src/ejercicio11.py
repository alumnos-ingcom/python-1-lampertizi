################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio5 import division_lenta
"""
Escribir una función que indique con True si un número entero es multiplo de otro,
utilizando sumas y restas.
PRE: n° entero

POST: valor booleano
"""

def es_multiplo(numero,multiplo):
    """
    Mediante 2 n° evalúa si el 2do es múltiplo del 1ero
    """
    if multiplo == 0:
        return False
    cociente, resto = division_lenta(numero,multiplo)
    if resto != 0:
        return False

    return True

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    numero = int(input("Ingrese un número: "))
    multiplo = int(input("Ingrese un posible múltiplo: "))

    resultado = es_multiplo(numero,multiplo)

    print(resultado)

if __name__ == "__main__":
    principal()
