from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, base:float=None, altura:float=None):
        super(Triangulo, self).__init__(ancho=base, alto=altura)

    def __str__(self):
        return f'Triangulo [base: {self._ancho}, altura: {self._alto}]'

    def calcular_area(self):
        return (self.alto*self.ancho)/2

    def calcular_perimetro(self):
        pass

if __name__ == '__main__':
    t1 = Triangulo(altura=3, base=9)
    print(t1)
    print(f'El area del triangulo es: {t1.calcular_area()}')