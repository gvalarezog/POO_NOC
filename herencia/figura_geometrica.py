from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    contador_figura = 0

    def __init__(self, ancho:float=0, alto:float=0):
        FiguraGeometrica.contador_figura += 1
        self._id = FiguraGeometrica.contador_figura
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return f'Figuara Geometrica: {self.__dict__.__str__()}'

    @property
    def id(self):
        return self._id

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