################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from ejercicio2 import signo

"""
Escribir una función que haga la suma entre dos números enteros
sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre 4 y 3,
las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

PRE: 2 n°enteros
POST: obtener el resultado de la suma como si se hiciera normalmente
"""

def suma_lenta(numero, otro_numero):
    """
    Hace la adición de 2 n° sumando de a 1
    """
    count = otro_numero
    temporal = numero

    if signo(otro_numero) == "positivo":
        while count > 0:
            numero = numero + 1
            count = count - 1
        veces_sumadas = " + 1" * otro_numero
        return f"{temporal}{veces_sumadas} = {numero}"

    elif signo(otro_numero) == "negativo":

        while count < 0 :
            numero = numero - 1
            count = count + 1

        veces_restadas = " - 1" * abs(otro_numero)

        return f"{temporal}{veces_restadas} = {numero}"

    else:
        return f"{numero} + {otro_numero} = {numero}"

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    num1 , num2 = int(input("1er numero: ")) , int(input("2do numero: "))

    resultado = suma_lenta(num1,num2)
    print(resultado)

if __name__ == "__main__":
    principal()
