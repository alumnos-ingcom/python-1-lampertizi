################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
PRE: string con una palabra/frase
POST: valor booleano indicando si es palíndromo o no
"""

def es_palindromo(texto):
    """
    Analiza un string e indica si es palíndromo o no con un valor booleano
    """
    count = 0
    letras_correctas = 0
    count_inverso = -1
    texto = texto.lower()
    while count < len(texto):
        if texto[count] == texto[count_inverso]:
            letras_correctas = letras_correctas + 1
            count_inverso = count_inverso - 1
            count = count + 1 
        else:
            count = count + 1
            
    if letras_correctas == len(texto):
        return True
    else:
        return False

def principal():
    x = input("Ingrese frase posiblemente palindrómica: ")
    resultado = es_palindromo(x)
    print(resultado)

if __name__ == "__main__":
    principal()
    