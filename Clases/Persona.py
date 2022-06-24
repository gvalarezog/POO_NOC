
class Persona:
    def __init__(self, nombre, genero, ocupacion):
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion

    def __str__(self):
        return f'Persona [nombre:{self._nombre}, genero: {self._genero}, ocupacion: {self._ocupacion}]'

    def obtenerNombre(self):
        return self._nombre

    def obtenerGenero(self):
        return self._genero

    def obtenerOcupacion(self):
        return self._ocupacion

    def modificarNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def modificarGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def modificarOcupacion(self, ocupacion):
        self._ocupacion = ocupacion

    def presentarse(self):
        genero = ''
        if self._genero == 'M':
            genero = 'Masculino'
        else:
            genero = 'Femenino'
        return f'El nombre de la persona es: {self.obtenerNombre()}, su genero es: {genero}'

'''
Esta seccion es para las pruebas de clase que se crea
'''

# objPersona1 = Persona.__init__(objPersona1, 'Luis', 'M', 'Estudiante')
objPersona1 = Persona('Luis', 'M', 'Estudiante')
print(type(objPersona1))
print(objPersona1._nombre) #incorrecto
print(objPersona1.obtenerNombre()) #correcto
print(f'El nombre de la persona es: {objPersona1.obtenerNombre()}')
# print(f'El nombre de la persona es: {objPersona1.obtenerNombre()}, su genero es: {objPersona1.obtenerGenero()}')
print(objPersona1.presentarse())
objPersona1._nombre = 'Marco' #incorrecta
objPersona1.modificarNombre('Carlos') #correcta
objPersona1.modificarOcupacion('Carpintero')
print(objPersona1)
print(objPersona1.__str__())
print('***********************')
objP2 = Persona('Maria', 'F', 'Docente')
print(f'El nombre de la persona es: {objP2._nombre}')
# print(f'El nombre de la persona es: {objP2._nombre}, su genero es: {objP2._genero}')
print(objP2.presentarse())
print(objP2.__str__())
objP3 = Persona('Diana', 'F', 'Chef')
print(objP3)
print(objP3.presentarse())



