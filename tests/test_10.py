################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
se probará la función que detecta frases/palabras palindrómicas
"""

def test_palindromico():
    """
    se insertarán frases palindromicas como tambien frases que no
    """
    frase1 = "hola aloh"
    frase2 = "neuquen"
    frase3 = "como andás jefe"
    frase4 = "ComOMOC"

    assert frase1 == True, "no detecta frases palindromicas"
    assert frase2 == True, "no detecta palabras palindromicas"
    assert frase3 == False, "no detecta frases no palindromicas"
    assert frase4 == True, "es case sensitive"

