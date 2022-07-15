

from empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'

    def mostrar_detalle(self):
        return f'El nombre del empleado es {self.nombre} con sueldo {self.sueldo} y pertenece al departamento {self.departamento}'


if __name__=='__main__':
    g = Gerente(nombre='Maria', sueldo=2000, departamento='TH')
    print(g)
    print(g.mostrar_detalle())