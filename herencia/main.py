from circunferencia import Circunferencia
from cuadrado import Cuadrado
from rectangulo import Rectangulo

c1 = Cuadrado(lado=5)
c2 = Cuadrado(lado=6)
c3 = Cuadrado(lado=7)
c4 = Cuadrado(lado=8)
c5 = Cuadrado(lado=9)

r1 = Rectangulo(base=5, altura=7)
r2 = Rectangulo(base=6, altura=8)
r3 = Rectangulo(base=7, altura=9)

cir1 = Circunferencia(radio=3)
cir2 = Circunferencia(radio=4)
cir3 = Circunferencia(radio=5)

print(f'Perimetro: {c1.calcular_perimetro()}')
print(f'Perimetro: {r1.calcular_perimetro()}')
print(f'Perimetro: {cir1.calcular_perimetro()}')
print('*'.center(50,'*'))
#vesrion del caclulo sin polimorfismo
print('vesrion del caclulo sin polimorfismo')
suma_perimetros = c1.calcular_perimetro() + r1.calcular_perimetro() + cir1.calcular_perimetro() \
                  + c2.calcular_perimetro() + r2.calcular_perimetro() + cir2.calcular_perimetro() \
                  + c3.calcular_perimetro() + r3.calcular_perimetro() + cir3.calcular_perimetro() \
                + c4.calcular_perimetro() + c5.calcular_perimetro()
print(f'Suma Total de Perimetros: {suma_perimetros}')

#vesrion del calculo con polimorfismo
print('vesrion del caclulo con polimorfismo')
def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total += figura.calcular_perimetro()
    return total

def detalle_figuras(figuras):
    cuadrado = 0
    rectangulo = 0
    for figura in figuras:
        if isinstance(figura, Cuadrado):
            cuadrado += 1
        elif isinstance(figura, Rectangulo):
            rectangulo += 1
    print(f'Cuadrados: {cuadrado}, Rectangulos: {rectangulo}')

figuras = [c1, r1, cir1, c2, r2, cir2, c3, r3, cir3, c4, c5]
print(f'Suma Total de Perimetros: {sumar_perimetros(figuras)}')
detalle_figuras(figuras)