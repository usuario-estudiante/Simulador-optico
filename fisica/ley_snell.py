import math as m
INCIDENCIA = 200
def __calcularX2(x1,y1,y2,angulo):
    x2 = x1 + ((y2 - y1)*(m.tan(m.radians(angulo))))
    return x2

def ley_snell(x1,y1,y2,angulo,n1,n2):
    x2 = __calcularX2(x1,y1,y2,angulo)
    angulo_incidencia = m.degrees(m.atan2(abs(x2-x1),abs(y2-y1)))
    angulo_refraccion = m.degrees(m.asin((n1 * m.sin(m.radians(angulo_incidencia))) / n2))
    return angulo_refraccion


    