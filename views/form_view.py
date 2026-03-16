from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QDoubleSpinBox, QPushButton, QLabel, QHBoxLayout,
    QMessageBox
)

from PySide6.QtCore import Qt

from services.mascota_service import MascotaService


class FormView(QWidget):

    def __init__(self, callback_cancelar=None, callback_guardado=None):
        super().__init__()

        self.callback_cancelar = callback_cancelar
        self.callback_guardado = callback_guardado

        self.mascota_id_actual = None

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.setContentsMargins(100, 50, 100, 50)

        # TITULO
        self.lbl_titulo = QLabel("🐾 Registro de Nueva Mascota")
        self.lbl_titulo.setStyleSheet(
            "font-size: 20pt; font-weight: bold; margin-bottom: 20px;"
        )
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(self.lbl_titulo)

        # FORMULARIO
        self.form_container = QWidget()

        self.form_layout = QFormLayout(self.form_container)
        self.form_layout.setSpacing(15)

        self.txt_nombre = QLineEdit()
        self.txt_especie = QLineEdit()

        self.txt_peso = QDoubleSpinBox()
        self.txt_peso.setRange(0.1, 100.0)
        self.txt_peso.setSuffix(" kg")

        self.form_layout.addRow("Nombre:", self.txt_nombre)
        self.form_layout.addRow("Especie:", self.txt_especie)
        self.form_layout.addRow("Peso:", self.txt_peso)

        self.main_layout.addWidget(self.form_container)

        # BOTONES
        self.button_layout = QHBoxLayout()

        self.btn_guardar = QPushButton("💾 Guardar")
        self.btn_guardar.setStyleSheet(
            "background-color: #2e7d32; padding: 10px; font-weight: bold;"
        )

        self.btn_cancelar = QPushButton("❌ Cancelar")

        # BOTÓN ELIMINAR
        self.btn_eliminar = QPushButton("🗑️ Eliminar Registro")
        self.btn_eliminar.setStyleSheet(
            "background-color: #c62828; padding: 10px; font-weight: bold;"
        )
        self.btn_eliminar.setVisible(False)

        self.btn_guardar.clicked.connect(self.procesar_y_guardar)
        self.btn_eliminar.clicked.connect(self.confirmar_eliminacion)

        if self.callback_cancelar:
            self.btn_cancelar.clicked.connect(self.callback_cancelar)

        self.button_layout.addWidget(self.btn_guardar)
        self.button_layout.addWidget(self.btn_cancelar)
        self.button_layout.addWidget(self.btn_eliminar)

        self.main_layout.addLayout(self.button_layout)

    def cargar_datos(self, mascota_id):

        mascota = MascotaService.obtener_por_id(mascota_id)

        if mascota:

            self.mascota_id_actual = mascota_id

            self.lbl_titulo.setText(
                f"✏️ Editando a: {mascota.nombre}"
            )

            self.txt_nombre.setText(mascota.nombre)
            self.txt_especie.setText(mascota.especie)
            self.txt_peso.setValue(mascota.peso)

            # mostrar botón eliminar
            self.btn_eliminar.setVisible(True)

        else:

            QMessageBox.critical(
                self,
                "Error",
                "No se encontró la mascota."
            )

    def limpiar_formulario(self):

        self.mascota_id_actual = None

        self.lbl_titulo.setText("🐾 Registro de Nueva Mascota")

        self.txt_nombre.clear()
        self.txt_especie.clear()
        self.txt_peso.setValue(0.1)

        self.btn_eliminar.setVisible(False)

    def procesar_y_guardar(self):

        nombre = self.txt_nombre.text().strip()
        especie = self.txt_especie.text().strip()
        peso = self.txt_peso.value()

        if not nombre or not especie:

            QMessageBox.warning(
                self,
                "Campos obligatorios",
                "Por favor completa nombre y especie."
            )

            return

        if self.mascota_id_actual:

            exito = MascotaService.actualizar(
                self.mascota_id_actual,
                nombre,
                especie,
                peso
            )

            mensaje = f"¡Datos de {nombre} actualizados!"

        else:

            exito = MascotaService.crear(
                nombre,
                especie,
                peso
            )

            mensaje = f"¡{nombre} ha sido registrado!"

        if exito:

            QMessageBox.information(
                self,
                "Éxito",
                mensaje
            )

            self.limpiar_formulario()

            if self.callback_guardado:
                self.callback_guardado()

        else:

            QMessageBox.critical(
                self,
                "Error",
                "No se pudo procesar la solicitud."
            )

    def confirmar_eliminacion(self):

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Estás seguro de eliminar este registro?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:

            if MascotaService.eliminar(self.mascota_id_actual):

                QMessageBox.information(
                    self,
                    "Eliminado",
                    "La mascota fue eliminada."
                )

                self.limpiar_formulario()

                if self.callback_guardado:
                    self.callback_guardado()