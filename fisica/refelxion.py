import math as m
def calcularReflexion(x, y, angulo, longitud):
    x2 = x + longitud * m.sin(m.radians(angulo))
    y2 = y - longitud * m.cos(m.radians(angulo))
    return x2, y2