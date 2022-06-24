
class Estudiante:
  def __init__(self, nombre, carrera, nivel):
    self._nombre = nombre
    self._carrera = carrera
    self._nivel = nivel

  def __str__(self):
    return f'Estudiante [nombre: {self._nombre}, carrera: {self._carrera}, nivel: {self._nivel}]'

  def obtenerNombre(self):
    return self._nombre

  def modifcarNombre(self, nombre):
    self._nombre = nombre

  def obtenerCarrera(self):
    return self._carrera

  def modificarCarrera(self, carrera):
    self._carrera = carrera

  def obtenerNivel(self):
    return self._nivel

  def modificarNivel(self, nivel):
    self._nivel = nivel

'''
Prueba de la clase estudiante
'''
e1 = Estudiante('Luis', 'LGIG', 3)
nombre = 'Carla'
carrera = 'AD'
nivel = 5

e2 = Estudiante(nombre, carrera, nivel)

print(e1)
print(e2)

a='CPA'
b=3
c='Manuel'
e3 = Estudiante(carrera = a, nivel= b, nombre =c)
print(e3)