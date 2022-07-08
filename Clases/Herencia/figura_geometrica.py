from abc import ABC, abstractmethod


#ABC = Abstract Base Class


class FiguraGeometrica(ABC):
    """
    Clase para herencia de FG
    """
    def __init__(self, ancho:float=None, alto:float=None):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return f'Figura Geometrica [ancho: {self._ancho}, alto: {self._alto}]'

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

if __name__ == '__main__':
    pass
