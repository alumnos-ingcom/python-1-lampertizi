################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
PRE: un n° entero
POST: un valor booleano
"""

def es_primo(numero):
    """
    Devuelve un bool indicando si el n° es primo o no
    """
    count = 1
    divisores = []

    while count <= numero:
        if numero % count == 0:
            divisores.append(count)
        count = count + 1

    if len(divisores) == 2:
       return True
    
    return False

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    num = int(input("Ingrese un n° positivo: "))
    resultado = es_primo(num)
    print(resultado) 

if __name__ == "__main__":
    principal()
