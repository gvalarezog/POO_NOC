

class Color:
    """
    Documentar la clase
    """
    def __init__(self, nombre:str=None):
        self._nombre = nombre

    def __str__(self):
        return f'Color [nombre: {self._nombre}]'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

if __name__ == '__main__':
    c = Color(nombre='Amarillo')
    print(c)