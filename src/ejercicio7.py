################
# Tiziano Lamperti - @lampertizi
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado expresado en 
grados, minutos y segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
PRE: de 1 a 3 valores enteros

POST: su respectiva conversión
"""
def sexagesimal_a_segundos(grados,minutos,segundos):
    
    assert grados or minutos or segundos > 0, "no existe el tiempo negativo"
    
    """
    Convierte de grados minutos y segundos a segundos
    """
    grados = grados * 3600
    minutos = minutos * 60
    cuenta = grados + minutos + segundos
    return cuenta

def segundos_a_sexagesimal(segundos):
    """
    Convierte los segundos a grados sexagesimales
    """
    assert segundos > 0, "no existe el tiempo negativo"
    grados = 0
    minutos = 0
    seconds = 0
    seg_input = segundos
    while seg_input >= 3600:
        seg_input = seg_input - 3600
        grados = grados + 1
    while seg_input >= 60:
        seg_input = seg_input - 60
        minutos = minutos + 1
    seconds = seconds + seg_input
    return (grados,minutos,seconds)

def principal():
    """
    Ésta función es la que interactúa con el usuario.
    """
    segundos = int(input("Cuántos segundos se quieren transformar?: "))

    resultado = segundos_a_sexagesimal(segundos)

    print(resultado)

    grados = int(input("grados a convertir: "))
    minutos = int(input("minutos a convertir: "))
    segundos = int(input("segundos a convertir: "))

    resultado2 = sexagesimal_a_segundos(grados,minutos,segundos)
    print(resultado2)

if __name__ == "__main__":
    principal()
    
