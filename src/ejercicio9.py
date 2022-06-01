################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio8 import es_primo
"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
PRE: un n° entero positivo
POST: tupla con todos los divisores primos del n° ingresado
"""

def factores_primos(numero):
    """
    Encuentra múltiplos primos del n° ingresado
    """
    n_primos = []
    count = 1
    while count <= abs(numero):    # se obtienen los n° primos hasta el n° pedido
        if es_primo(count):
            n_primos.append(count)
        count = count + 1

    count = 0                       #
    temp = abs(numero)              #
    if numero < 0:                  #
        factores = [-1]             # lista final de factores primos para n° negativos
    else:
        factores = []               #
    while temp > 1:
        factor_primo = n_primos[count]

        if temp % factor_primo == 0: # encuentra los factores repetidos
            temp = temp // factor_primo
            factores.append(factor_primo)
        else:
            count = count + 1 #pasa al siguiente n° primo
    return tuple(factores)

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    num = int(input("Ingrese un n° positivo: "))
    resultado = factores_primos(num)
    print(resultado)

if __name__ == "__main__":
    principal()
    
