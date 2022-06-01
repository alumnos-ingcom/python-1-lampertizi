################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio1 import celsius_a_fahrenheit, fahrenheit_a_celsius

"""
Se probarán las funciones de conversion de T°
"""

def test_fahrenheit():
    """
    se insertarán valores negativos, 0 y float
    """
    res2 = 0.27222222222222336
    res3 = -17.77777777777778
    assert fahrenheit_a_celsius(-4) == -20.0, "no funciona con n° negativos"
    assert fahrenheit_a_celsius(32.49) == res2, "no funciona con floats"
    assert fahrenheit_a_celsius(0) == res3, "no detecta al cero"

def test_celsius():
    """
    se insertarán valores negativos,0 y float
    """
    assert celsius_a_fahrenheit(-5) == 23, "no funciona con n° negativos"
    assert celsius_a_fahrenheit(41.65) == 106.97, "no funciona con floats"
    assert celsius_a_fahrenheit(0) == 32.0, "no detecta al cero"

def test_general():
    """
    se ingresará una función dentro de otra, esperando obtener el resultado ingresado
    """
    assert celsius_a_fahrenheit(fahrenheit_a_celsius(32)) == 32, "no funciona la conversión"
    