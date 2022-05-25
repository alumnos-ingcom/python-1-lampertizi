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
    count = 1
    divisores = []

    while count <= numero:
        if numero % count == 0:
            divisores.append(count)
        count = count + 1

    if len(divisores) == 2:
       return True 
    else:
        return False

def principal():
    x = int(input("Ingrese un n° positivo: "))
    resultado = es_primo(x)
    print(resultado) 

if __name__ == "__main__":
    principal()