from empleado import Empleado
from gerente import Gerente


def imprimir_detalles(objecto):
    if isinstance(objecto, Gerente):
        print('Los datos del Gerente son:')
    else:
        print('Los datos del Empleado son:')
    print(objecto.mostrar_detalle())

def imprimir(objecto):
    print(objecto.mostrar_detalle())


if __name__ == '__main__':
    e = Empleado(nombre='Luis', sueldo=1000)
    g = Gerente(nombre='Maria', sueldo=2000, departamento='TH')
    g1 = Gerente(nombre='Maria', sueldo=2000, departamento='SIS')
    g2 = Gerente(nombre='Maria', sueldo=2000, departamento='COM')
    g3 = Gerente(nombre='Maria', sueldo=2000, departamento='SAC')

    imprimir_detalles(e)
    imprimir_detalles(g)
    imprimir_detalles(g1)
    imprimir_detalles(g2)
    imprimir_detalles(g3)


