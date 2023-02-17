import sys

from PySide6.QtWidgets import QApplication
from servicio.persona_ingreso import PersonaIngreso

app = QApplication()
vtn_persona_ingreso = PersonaIngreso()
vtn_persona_ingreso.show()
sys.exit(app.exec())