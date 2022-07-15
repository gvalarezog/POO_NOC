from test_polimorfismo import imprimir_detalles, imprimir
from empleado import Empleado
from gerente import Gerente

e = Empleado(nombre='Luis', sueldo=1000)
g = Gerente(nombre='Maria', sueldo=2000, departamento='TH')


imprimir_detalles(g)
imprimir(e)


