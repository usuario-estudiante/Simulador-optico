import math as m
from .ley_snell import leySnell as ls

def calcularPuntos(x2,y2,angulo,longitud):
    x1  = x2 - longitud * m.sin(m.radians(angulo))
    y1  = y2 - longitud * m.cos(m.radians(angulo))
    return x1,y1

def calcularRayoRefractado(angulo_incidente, n1, n2):
    angulo = ls(angulo_incidente,n1,n2)
    x3 = 400 + 300 * m.sin(m.radians(angulo))
    y3 = 300 + 300 *m.cos(m.radians(angulo))
    return x3,y3
    