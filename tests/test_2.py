################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio2 import signo

"""
se probará la indicación del signo del n° ingresado
"""

def test_de_signos():
    """
    se ponen a prueba los 4 posibles casos
    """
    assert signo(-15) == "negativo", "no se puede determinar el valor negativo"
    assert signo(32) == "positivo", "no se puede determinar el valor positivo"
    assert signo(0) == "cero", "no se puede determinar el cero"
    assert signo(65.4) == "positivo", "no puede calcular con n° decimales"
