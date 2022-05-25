################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from ejercicio5 import division_lenta
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
    if "resto = 0" not in division_lenta(numero,multiplo):
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
