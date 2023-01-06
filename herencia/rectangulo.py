from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):

    def __init__(self, base:float=0, altura:float=0):
        super(Rectangulo, self).__init__(ancho=base, alto=altura)

    def __str__(self):
        return f'Rectagulo: [id: {self.id}, altura: {self.alto}, base: {self.ancho}]'

    def calcular_area(self):
        return self.alto*self.ancho

    def calcular_perimetro(self):
        return self.alto * 2 + self.ancho * 2

if __name__ == '__main__':
    r1 = Rectangulo(base=16, altura=10)
    print(r1)
    print(f'El area es: {r1.calcular_area()}')
    print(f'__name__: {__name__}')
