import re

from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from GUI.persona_ingreso import Ui_vtn_persona_ingreso
from PySide6 import QtGui
from datos.archivo import Archivo
from dominio.persona import Persona



class PersonaIngreso(QMainWindow):
    def __init__(self):
        super(PersonaIngreso, self).__init__()
        self.ui = Ui_vtn_persona_ingreso()
        self.ui.setupUi(self)
        self._persona = None
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_formulario)

        rx = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(rx, self)
        self.ui.txt_email.setValidator(validator)

        rx_ip = r'^((0|[1-9][0-9]?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.|$)){4}$'
        validator = QRegularExpressionValidator(rx_ip, self)
        self.ui.txt_ip.setValidator(validator)


    def grabar(self):
        if self.validar_formulario():
            self.capturar_datos()
            print(self._persona)
            if Archivo.guardar(self._persona):
                self.ui.stb_estado.showMessage('Se guardo con éxito.', timeout=5000)
                self.limpiar_formulario()
            else:
                QMessageBox.critical(self, 'Error', 'Error al guardar los datos en el archivo.')
        else:
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios.')
            print('Faltan datos')

    def limpiar_formulario(self):
        self.ui.txt_cedula.setText('')
        self.ui.txt_nombre1.setText('')
        self.ui.txt_nombre2.setText('')
        self.ui.txt_apellido_paterno.setText('')
        self.ui.txt_apellido_materno.setText('')
        self.ui.txt_ip.setText('')
        self.ui.cb_color_preferido.setCurrentText('Amarillo')
        self.ui.txt_email.setText('')
        self.ui.spb_edad.setValue(0)
        self._persona = None

    def capturar_datos(self):
        if not self._persona:
            self._persona = Persona()
        self._persona.nombre1 = self.ui.txt_nombre1.text()
        self._persona.nombre2 = self.ui.txt_nombre2.text()
        self._persona.apellido_paterno = self.ui.txt_apellido_paterno.text()
        self._persona.apellido_materno = self.ui.txt_apellido_materno.text()
        self._persona.email = self.ui.txt_email.text()
        self._persona.cedula = self.ui.txt_cedula.text()
        self._persona.sexo = self.ui.cb_sexo.currentText()
        self._persona.fecha_nacimiento = self.ui.date_fecha_nacimiento.text()
        self._persona.edad = self.ui.spb_edad.text()
        self._persona.color_preferido = self.ui.cb_color_preferido.currentText()
        self._persona.ip = self.ui.txt_ip.text()

    def validar_formulario(self):
        return (self.ui.txt_nombre1.text() != '' and self.ui.txt_apellido_paterno.text() != '' and
                self.ui.txt_apellido_materno.text() != '' and
                len(self.ui.txt_cedula.text()) == 10 and self.validar_email(self.ui.txt_email.text()))

    def validar_email(self, email):
        # expresionRegular = r'(^[\w]+)@([\w]+)' + '{2,3}'
        expresionRegular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.search(expresionRegular, email)

