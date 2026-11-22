import math as m
INCIDENCIA = 300


def leySnell(angulo,n1,n2):
    angulo_refraccion = n1 * m.sin(m.radians(angulo)) / n2
    if(abs(angulo_refraccion)>1):
        return None
    return m.degrees(m.asin(angulo_refraccion))


    