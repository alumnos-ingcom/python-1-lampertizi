################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio6 import menor_a_mayor, mayor_a_menor

"""
se probarán las funciones que ordenan de mayor a menor y viceversa
"""

def test_menormayor():
    """
    se evaluarán valores neutros, repetidos y negativos
    """
    caso_negativos = menor_a_mayor(-12,-65,-19)
    caso_neutros = menor_a_mayor(0,9,6)
    caso_repetidos = menor_a_mayor(7,7,90)

    assert caso_negativos == (-65, -19, -12), "no ordena valores negativos"
    assert caso_neutros == (0, 6, 9), "no ordena con valor neutro"
    assert caso_repetidos == (7, 7, 90), "no ordena valores repetidos"


def test_mayormenor():
    """
    se evaluarán valores neutros, repetidos y negativos
    """

    caso_negativos = mayor_a_menor(-12,-65,-19)
    caso_neutros = mayor_a_menor(0,9,6)
    caso_repetidos = mayor_a_menor(7,7,90)

    assert caso_negativos == (-12, -19, -65), "no ordena valores negativos"
    assert caso_neutros == (9, 6, 0), "no ordena con valor neutro"
    assert caso_repetidos == (90, 7, 7), "no ordena valores repetidos"
