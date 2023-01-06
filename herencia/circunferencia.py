from figura_geometrica import FiguraGeometrica
import math

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio:float=0):
        super(Circunferencia, self).__init__(ancho=radio)

    def __str__(self):
        return f'Circunferencia: [id: {self.id}, radio: {self.ancho}]'

    def calcular_area(self):
        return (self.ancho * self.ancho) * math.pi

    def calcular_perimetro(self):
        return 2 * math.pi * self.ancho

if __name__ == '__main__':
    c1 = Circunferencia(radio=4)
    print(c1)
    print(f'El area es: {c1.calcular_area()}')