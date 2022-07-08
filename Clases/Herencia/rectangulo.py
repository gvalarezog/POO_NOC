from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, base:float=None, altura:float=None):
        super(Rectangulo, self).__init__(ancho=base, alto=altura)

    def __str__(self):
        return f'Rectangulo [base: {self._ancho}, altura: {self._alto}]'

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return self.alto*2 + self.ancho*2

if __name__ == '__main__':
    r1 = Rectangulo(altura=3, base=9)
    print(r1)
    print(f'El area del rectagulo es: {r1.calcular_area()}')
    print(f'El perimetro del rectagulo es: {r1.calcular_perimetro()}')