from color import Color
from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, lado:float=0, color:str=None):
        # super(Cuadrado, self).__init__(ancho=lado, alto=lado)
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        # super(Cuadrado, self).__init__(color=color)
        Color.__init__(self, color=color)

    def __str__(self):
        return f'Cuadrado: [id: {self.id}, lado: {self.alto}, color: {self.color}]'

    def calcular_area(self):
        return self.alto * self.alto

    def calcular_perimetro(self):
        return 2 * self.alto

if __name__ == '__main__':
    c1 = Cuadrado(lado=16, color='celeste')
    print(c1)
    print(f'El area es: {c1.calcular_area()}')
    print(Cuadrado.mro())