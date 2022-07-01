

class Vehiculo:
    """
    La clase permite crear objetos de tipo vehiculo
    Autor: Guillermo Valarezo Guzmán
    """
    def __init__(self, marca:str=None, modelo:str=None, anio:int= 1890, matriculado:bool= False, placa:str=''):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._matriculado = matriculado
        self._placa = placa

    def __str__(self):
        return f'Vehiculo [marca: {self._marca}, modelo: {self._modelo}, año: {self._anio}, ' \
               f'matriculado?: {self._matriculado}, placa: {self._placa}]'

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def matriculado(self):
        return self._matriculado

    @matriculado.setter
    def matriculado(self, matriculado):
        self._matriculado = matriculado

    # Read Only - Solo lectura
    @property
    def placa(self):
        return self._placa

    # @placa.setter
    # def placa(self, placa):
    #     self.__placa = placa


if __name__ == "__main__":
    v1 = Vehiculo('Ford', 'F150', 2020, True)
    # print(v1)

    # v1.matriculado = False
    print(v1)
    print(v1.marca)
    # print(v1._marca) asi no se debe usar

    print(v1.modelo)
    v1.modelo = 'Fiesta'
    print(v1.modelo)
    # v1._modelo = 'Escape' asi no se debe usar
    print(v1.modelo)
    print(v1)

    v2 = Vehiculo('Kia', 'Rio')
    v2.anio = 2020
    print(v2)

    v3 = Vehiculo ('Lada')
    print(v3)

    v4 = Vehiculo(marca='Chevrolet', modelo='Sail', anio=2020, matriculado=True)
    print(v4)

    v5 = Vehiculo(marca='Mazda', modelo='BT50', anio='Dos mil veinti dos', matriculado=True)
    print(v5)
    print(type(v5.marca))
    print(type(v5.modelo))
    print(type(v5.anio))
    print(type(v5.matriculado))

    v6 = Vehiculo(marca='Mitsubishi')
    print(v6)

    v7 = Vehiculo(marca='Mitsubishi')
    print(v7)

    print(v6.marca == v5.marca)

    v8 = Vehiculo(placa='GPO-1234')
    v8.marca = 'Suzuki'
    v8.modelo = 'Forza'
    v8.anio = '1990'
    v8.matriculado = True
    print(v8)
    # v8.placa = 'GPO-1233'
    # print(v8)
    # v8.placa = 'GPO-1233'
    # v8._placa = 'asbcded'
    print(v8)




