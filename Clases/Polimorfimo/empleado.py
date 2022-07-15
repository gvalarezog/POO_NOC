
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalle(self):
        return f'El nombre del empleado es {self.nombre} con sueldo {self.sueldo}'

if __name__=='__main__':
    e = Empleado(nombre='Luis', sueldo=1000)
    print(e)
    print(e.mostrar_detalle())