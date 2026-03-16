import sys
import qdarkstyle

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QToolBar
)

from PySide6.QtGui import QAction

from views.home_view import HomeView
from views.form_view import FormView


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("🐾 PySide Mascotas")
        self.setMinimumSize(1280, 720)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # FORM VIEW
        def al_guardar():
            self.home_view.actualizar_tabla()
            self.stack.setCurrentIndex(0)

        self.form_view = FormView(
            callback_cancelar=lambda: self.stack.setCurrentIndex(0),
            callback_guardado=al_guardar
        )

        # FUNCIÓN PARA PREPARAR EDICIÓN
        def preparar_edicion(id_m):

            self.form_view.cargar_datos(id_m)
            self.stack.setCurrentIndex(1)

        # HOME VIEW
        self.home_view = HomeView(
            callback_editar=preparar_edicion
        )

        self.stack.addWidget(self.home_view)
        self.stack.addWidget(self.form_view)

        self.crear_menu()

    def crear_menu(self):

        toolbar = QToolBar("Navegación Principal")
        self.addToolBar(toolbar)

        btn_inicio = QAction("🏠 Inicio", self)
        btn_inicio.triggered.connect(
            lambda: self.stack.setCurrentIndex(0)
        )

        toolbar.addAction(btn_inicio)

        btn_agregar = QAction("➕ Agregar Mascota", self)

        def abrir_formulario():
            self.form_view.limpiar_formulario()
            self.stack.setCurrentIndex(1)

        btn_agregar.triggered.connect(abrir_formulario)

        toolbar.addAction(btn_agregar)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setStyleSheet(
        qdarkstyle.load_stylesheet_pyside6()
    )

    window = MainWindow()
    window.show()

    sys.exit(app.exec())