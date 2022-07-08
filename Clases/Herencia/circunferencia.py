from figura_geometrica import FiguraGeometrica
import math

class Circunferencia(FiguraGeometrica):
    def __init__(self, radio:float=None):
        super(Circunferencia, self).__init__(alto=radio, ancho=None)

    def __str__(self):
        return f'Circunferencia [radio: {self.alto}]'

    def calcular_area(self):
        return self.alto*self.alto*math.pi

    def calcular_perimetro(self):
        pass

if __name__ == '__main__':
    cir1 = Circunferencia(radio=7)
    print(cir1)
    print(f'El area de la circunferncia es: {cir1.calcular_area()}')
