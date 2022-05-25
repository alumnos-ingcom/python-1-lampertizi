################ # Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

 -1 si el primero es menor que el segundo
  0 si son iguales
  1 si el primero es mayor que el segundo

PRE: dos números reales

POST: obtener un valor entre -1 y 1 que indique una igualdad o desigualdad entre los 2 valores
"""

def compara(numero, otro_numero):
    """
    Determina la igualdad o desigualdad entre 2 valores dados
    """
    if numero - otro_numero == 0:
        return 0
    elif numero - otro_numero > 0:
        return 1
    else:
        return -1

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    num1 = float(input("Ingresá un n° a comparar: "))
    num2 = float(input("Ingresá otro n° a comparar: "))
    resultado = compara(num1,num2)
    print(resultado)


if __name__ == "__main__":
    principal()
