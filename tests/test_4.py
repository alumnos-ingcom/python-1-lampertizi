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
    res1 = "5 + 1 + 1 + 1 = 8"
    res2 = "4 - 1 - 1 = 2"
    res3 = "9 + 0 = 9"
    res4 = "0 - 1 - 1 - 1 = -3"

    assert suma_lenta(5,3) == res1, "error en la suma"
    assert suma_lenta(4,-2) == res2, "error en la resta"
    assert suma_lenta(9,0) == res3,"error cuando se suma cero"
    assert suma_lenta(0,-3) == res4, "error cuando se le resta a cero"
