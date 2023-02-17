

class Persona:
    def __init__(self, cedula=None, nombre1=None, nombre2=None,
                apellido_paterno=None, apellido_materno=None,
                 email=None, edad=None, fecha_nacimiento=None,
                 color_preferido = None, sexo=None, ip=None):
        self._cedula = cedula
        self._nombre1 = nombre1
        self._nombre2 = nombre2
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._email = email
        self._edad = edad
        self._fecha_nacimiento = fecha_nacimiento
        self._color_preferido = color_preferido
        self._sexo = sexo
        self._ip = ip

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre1(self):
        return self._nombre1

    @nombre1.setter
    def nombre1(self, nombre1):
        self._nombre1 = nombre1

    @property
    def nombre2(self):
        return self._nombre2

    @nombre2.setter
    def nombre2(self, nombre2):
        self._nombre2 = nombre2

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self, apellido_paterno):
        self._apellido_paterno = apellido_paterno

    @property
    def apellido_materno(self):
        return self._apellido_materno

    @apellido_materno.setter
    def apellido_materno(self, apellido_materno):
        self._apellido_materno = apellido_materno

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def color_preferido(self):
        return self._color_preferido

    @color_preferido.setter
    def color_preferido(self, color_preferido):
        self._color_preferido = color_preferido

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    def __str__(self):
        return f'Persona {self.__dict__.__str__()}'

if __name__ == '__main__':
    p1 = Persona(cedula='012345689', nombre1='Luis', apellido_paterno='Perez')
    print(p1)
