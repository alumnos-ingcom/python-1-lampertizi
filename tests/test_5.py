################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio5 import division_lenta
"""
se probará la función que hace una division de a pasos / lenta
"""

def test_division_lenta():
    """
    se probarán valores negativos y positivos
    """
    assert division_lenta(18,2) == (9,0),"error en la división con resto cero"
    assert division_lenta(18,5) == (3,3), "error en la division con resto != de cero"
    assert division_lenta(-78,2) == (-39,0), "no funciona con n° negativos"
    assert division_lenta(78,-2) == (-39,0), "no funciona con n° negativos"