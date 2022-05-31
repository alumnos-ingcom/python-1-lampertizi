################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio3 import compara

"""
se probarán los 3 posibles resultados (-1,0,1)
"""

def test_comparacion():
    """
    en base a los resultados esperados en 4 casos distintos se espera obtener feedback
    """
    assert compara(4,-3) == 1, "no funciona cuando se espera el valor 1"
    assert compara(-9,5) == -1, "no funciona cuando se espera el valor -1"
    assert compara(5,5) == 0, "no funciona cuando se espera el valor 0"
    assert compara(7.56,3.5) == 1, "no funciona cuando se ingresan floats y se espera el valor 1"
