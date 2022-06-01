################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

PRE: un n° real

POST: Obtener la conversión deseada
"""

def celsius_a_fahrenheit(centigrados):
    """
    Transforma los grados Celsius a grados Fahrenheit
    """
    cuenta = (centigrados * (9/5)) + 32
    return cuenta

def fahrenheit_a_celsius(fahrenheit):
    """
    Transforma los grados Fahrenheit a grados Celsius
    """
    cuenta = (fahrenheit - 32) * (5/9)
    return cuenta

def principal():
    """
    Ésta es la función que interactúa con el usuario
    """
    grados_celsius = float(input("Celsius a transformar: "))
    resultado1 = celsius_a_fahrenheit(grados_celsius)

    print(f"{grados_celsius} son {resultado1}F°")

    grados_fahrenheit = float(input("Fahrenheit a transformar: "))
    resultado2 = fahrenheit_a_celsius(grados_fahrenheit)

    print(f"{grados_fahrenheit}°F son {resultado2}°C")


if __name__ == "__main__":
    principal()
