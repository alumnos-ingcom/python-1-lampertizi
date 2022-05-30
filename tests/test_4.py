################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio4 import suma_lenta
"""
se probará el ejercicio de suma lenta
"""

def test_nombrefuncion():
    """
    se ingresarán valores tanto positivos como negativos y cero
    """
    assert suma_lenta(5,3) == "= 8", "error en la suma"
    assert suma_lenta(4,-2) == "= 2", "error en la resta"
    assert suma_lenta(9,0) == "= 9", "error cuando se suma cero"
    assert suma_lenta(0,-3) == "= -3", "error cuando se le resta a cero"
