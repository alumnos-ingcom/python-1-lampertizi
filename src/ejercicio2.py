################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.

PRE: Un n° real

POST: Indicar si es un n° positivo, negativo o cero
"""

def signo(numero):
    """
    Mediante una resta y una suma se sabrá el signo del n° ingresado.
    """
    if (numero-numero) > -(numero+numero):
        return "positivo"

    elif (numero+numero) < -(numero+numero):
        return "negativo"
    else:
        return "cero"

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    numero = float(input("ingresar un n° para saber su signo: "))

    resultado = signo(numero)
    print(resultado)

if __name__ == "__main__":
    principal()
