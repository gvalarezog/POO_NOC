

class Persona:

    def __init__(self, cedula=None, nombre=None, apellido=None, email=None, telefono=None):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono

    def __str__(self):
        return f'Persona [cedula: {self._cedula}, nombre: {self._nombre}, apellido: {self._apellido}, email: {self._email}]'

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula


if __name__ == '__main__':
    objPersona1 = Persona('123', 'Juan', 'Perez', 'jperez@mail.com')
    # objPersona2 = Persona('123', 'Juan', 'Perez')
    # objPersona3 = Persona('456', 'Maria', 'Garcia')
    # print(objPersona1)
    # print(objPersona2)
    # print(objPersona3)
    # objPersona2._cedula = '987'
    # print(objPersona2)
    # objPersona4 = Persona('6456', 'Luis', 'Paz')
    # print(objPersona4)
    # objPersona5 = Persona(email='mpaz@mail.com', apellido='Paz', nombre='MAria', cedula='5545456')
    # print(objPersona5)

    print(f'El # de cedula es: {objPersona1.cedula}')
    # print(f'El # de cedula es: {objPersona1._cedula}')
    # objPersona1._cedula = '0123456789'
    objPersona1.cedula = '0123456789'
    print(f'El # de cedula es: {objPersona1.cedula}')