from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    """
    Clase que hereda de FG
    """
    contador_cuadrado = 0
    def __init__(self, lado:float=None, activo:bool=True, color:str=None):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self, nombre=color)
        # super(Cuadrado, self).__init__(ancho=lado, alto=lado)
        # super(Cuadrado, self).__init__(nombre=color)
        self._activo = activo
        # Cuadrado.contador_cuadrado = Cuadrado.contador_cuadrado + 1
        Cuadrado.contador_cuadrado += 1
        self._id = Cuadrado.contador_cuadrado

    def __str__(self):
        return f'Cuadrado [id: {self._id}, lado: {self.alto}, activo: {self._activo}] {Color.__str__(self)} ' \
               f'{super().__str__()}'

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    @property
    def id(self):
        return self._id

    def calcular_area(self):
        return self.alto * self.ancho

    def calcular_perimetro(self):
        return self.alto*4


if __name__ == '__main__':
    c1 = Cuadrado(lado=7, activo=True, color='Amarillo')
    print(c1.__str__())
    print(f'El area del cuadrado es: {c1.calcular_area()}')
    print(f'El perimetro del cuadrado es: {c1.calcular_perimetro()}')
    print(Cuadrado.mro())
    c2 = Cuadrado()
    print(c2)
    c3 = Cuadrado(lado=6)
    print(c3)
    # print(c3.contador_cuadrado)
    print(Cuadrado.contador_cuadrado)
