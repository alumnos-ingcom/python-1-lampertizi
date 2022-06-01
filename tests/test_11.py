################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio11 import es_multiplo

"""
se probará la funcion que detecta multiplos entre 2 n°
"""

def test_multiplos():
    """
    se insertarán n° negativos, positivos, y neutros
    """
    
    assert es_multiplo(15,2) == False,"no detecta cuando no es multiplo"
    assert es_multiplo(98,2) == True, "no detecta cuando si es multiplo"
    assert es_multiplo(-40,5) == True, "no detecta cuando hay n° negativos"
    assert es_multiplo(18,-2) == True, "no detecta cuando hay n° negativos"
    assert es_multiplo(78,0) == AssertionError, "no frena la división por cero"
