################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio10 import es_palindromo

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

    assert es_palindromo(frase1) is True, "no detecta frases palindromicas"
    assert es_palindromo(frase2) is True, "no detecta palabras palindromicas"
    assert es_palindromo(frase3) is False, "no detecta frases no palindromicas"
    assert es_palindromo(frase4) is True, "es case sensitive"
