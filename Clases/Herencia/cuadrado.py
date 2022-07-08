from figura_geometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    """
    Clase que hereda de FG
    """
    def __init__(self, lado:float=None, activo:bool=True):
        super(Cuadrado, self).__init__(ancho=lado, alto=lado)
        self._activo = activo

    def __str__(self):
        return f'Cuadrado [lado: {self.alto}, activo: {self._activo}]'

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return self.alto*4


if __name__ == '__main__':
    c1 = Cuadrado(lado=7, activo=True)
    print(c1)
    print(f'El area del cuadrado es: {c1.calcular_area()}')
    print(f'El perimetro del cuadrado es: {c1.calcular_perimetro()}')
