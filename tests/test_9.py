################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio9 import factores_primos

"""
se probará la función que retorna una tuple de n° primos
"""

def test_factores():
    """
    se pondrán n° con factores primos repetidos, únicos y negativos
    """
    res1 = (2,2,2)
    res2 = (5,157)
    res3 = (-1,3,5)

    assert res1 == factores_primos(8), "no calcula factores iterados"
    assert res2 == factores_primos(785), "no calcula numeros grandes"
    assert res3 == factores_primos(-15), "no calcula n° negativos"
