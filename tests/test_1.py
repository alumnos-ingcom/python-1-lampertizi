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
    try:
        fahrenheit_a_celsius(-15)
        fahrenheit_a_celsius(32.49)
        fahrenheit_a_celsius(0)
    except:
        print("error en la conversion de F° a C°")

def test_celsius():
    """
    se insertarán valores negativos,0 y float
    """
    try:
        celsius_a_fahrenheit(-79)
        celsius_a_fahrenheit(41.65)
        celsius_a_fahrenheit(0)
    except:
        print ("error en la conversion de C° a F°")

def test_general():
    """
    se ingresará una función dentro de otra, esperando obtener el resultado ingresado
    """
    assert celsius_a_fahrenheit(fahrenheit_a_celsius(32)) == 32, "no funciona la conversión"
    