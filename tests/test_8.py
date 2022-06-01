################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio8 import es_primo
"""
se probará la función que detecta n° primos
"""

def test_primo():
    """
    se introducirán n° positivos no primos, primos, y negativos
    """
    assert es_primo(10) == False, "no calcula correctamente ante n° positivos no primos"
    assert es_primo(-7) == False, "no calcula correctamente n° negativos"
    assert es_primo(97) == True, "no calcula correctamente primos"
