import math as m
AIRE = 1.0003
AGUA = 1.333

INCIDENCIA = 200
def __calcuar_punto_incidencia(x1,y1,y2,angulo):
    x2 = x1 + ((y2 - y1)*(m.tan(m.radians(angulo))))
    return x2

def ley_snell(x1,y1,y2,angulo):
    punto_incidencia = __calcuar_punto_incidencia(x1,y1,y2,angulo)
    print(punto_incidencia)

ley_snell(100,50,INCIDENCIA,45)