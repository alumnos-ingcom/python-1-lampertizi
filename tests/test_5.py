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
    se probarán valores negativos, positivos y con cero
    """
    assert division_lenta(18,2) == (9,0),"error en la división con resto cero"
    assert division_lenta(18,5) == (3,3), "error en la division con resto != de cero" 
    assert division_lenta(15,0) == ZeroDivisionError,"puede dividir por cero O_o"
    assert division_lenta(-10,2) == (-5,0),"error en la división de n° negativos"
