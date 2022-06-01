################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio7 import sexagesimal_a_segundos, segundos_a_sexagesimal

"""
Se probarán las conversiones a grados sexagesimales y a segundos
"""

def test_sexa_a_seg():
    """
    se pondrán valores en cada variable solicitada
    """
    resultado1 = sexagesimal_a_segundos(0,2,0)
    resultado2 = sexagesimal_a_segundos(2,0,0)
    resultado3 = sexagesimal_a_segundos(0,0,18)

    assert resultado1 == 120, "no puede calcular minutos"
    assert resultado2 == 7200, "no puede calcular grados"
    assert resultado3 == 18, "no puede calcular segundos"

def test_seg_a_sexa():
    """
    se pondrán valores en ciertas variables
    """
    resultado1 = segundos_a_sexagesimal(79)
    resultado2 = segundos_a_sexagesimal(5)
    resultado3 = segundos_a_sexagesimal(6400)
    assert resultado1 == (0, 1, 19), "no calcula correctamente más de 1'"
    assert resultado2 == (0, 0, 5), "no puede calcular menos de 1' "
    assert resultado3 == (1, 46, 40), "no calcula más allá de la hora"

def test_general():
    """
    se obtendrá la salida de meter una función en la otra
    """
    numero = 8652
    grad,mins,seg = segundos_a_sexagesimal(numero)

    assert sexagesimal_a_segundos(grad,mins,seg) == 8652, "no convierte correctamente"
