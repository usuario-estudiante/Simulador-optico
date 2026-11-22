import math as m

def calcularPuntos(x2,y2,angulo,longitud):
    x1  = x2 - longitud * m.sin(m.radians(angulo))
    y1  = y2 - longitud * m.cos(m.radians(angulo))
    return x1,y1

