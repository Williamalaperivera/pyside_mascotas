from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableView,
    QHeaderView,
    QAbstractItemView,
    QLineEdit,
    QHBoxLayout,
    QPushButton
)

from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

from services.mascota_service import MascotaService

import matplotlib.pyplot as plt


class HomeView(QWidget):

    def __init__(self, callback_editar=None):

        super().__init__()

        self.callback_editar = callback_editar

        self.pagina_actual = 1
        self.registros_por_pagina = 10

        self.layout = QVBoxLayout(self)

        self.lbl_titulo = QLabel("🐾 Panel de Gestión de Mascotas")
        self.lbl_titulo.setStyleSheet("font-size: 24pt; font-weight: bold;")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.lbl_titulo)

        self.lbl_total = QLabel()
        self.lbl_promedio = QLabel()
        self.lbl_especies = QLabel()

        self.layout.addWidget(self.lbl_total)
        self.layout.addWidget(self.lbl_promedio)
        self.layout.addWidget(self.lbl_especies)

        # BOTON GRAFICA
        self.btn_grafica = QPushButton("📊 Ver gráfica de especies")
        self.btn_grafica.clicked.connect(self.mostrar_grafica)

        self.layout.addWidget(self.btn_grafica)

        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("🔎 Buscar por nombre o especie...")
        self.txt_buscar.textChanged.connect(self.filtrar_tabla)

        self.layout.addWidget(self.txt_buscar)

        self.tabla_mascotas = QTableView()

        self.tabla_mascotas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_mascotas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_mascotas.verticalHeader().setVisible(False)
        self.tabla_mascotas.setSortingEnabled(True)

        self.tabla_mascotas.doubleClicked.connect(self.on_double_click)

        self.layout.addWidget(self.tabla_mascotas)

        self.layout_paginacion = QHBoxLayout()

        self.btn_anterior = QPushButton("⬅ Anterior")
        self.btn_siguiente = QPushButton("Siguiente ➡")

        self.btn_anterior.clicked.connect(self.pagina_anterior)
        self.btn_siguiente.clicked.connect(self.pagina_siguiente)

        self.layout_paginacion.addWidget(self.btn_anterior)
        self.layout_paginacion.addWidget(self.btn_siguiente)

        self.layout.addLayout(self.layout_paginacion)

        self.actualizar_dashboard()
        self.actualizar_tabla()

    def actualizar_dashboard(self):

        stats = MascotaService.obtener_estadisticas()

        self.lbl_total.setText(f"Total de mascotas: {stats['total']}")
        self.lbl_promedio.setText(f"Peso promedio: {stats['promedio_peso']} kg")
        self.lbl_especies.setText(f"Especies registradas: {stats['especies']}")

    def actualizar_tabla(self):

        self.mascotas = MascotaService.obtener_todos()

        inicio = (self.pagina_actual - 1) * self.registros_por_pagina
        fin = inicio + self.registros_por_pagina

        mascotas_pagina = self.mascotas[inicio:fin]

        self.model = QStandardItemModel(len(mascotas_pagina), 4)

        self.model.setHorizontalHeaderLabels(
            ["ID", "Nombre", "Especie", "Peso"]
        )

        for fila, m in enumerate(mascotas_pagina):

            self.model.setItem(fila, 0, QStandardItem(str(m.id)))
            self.model.setItem(fila, 1, QStandardItem(m.nombre))
            self.model.setItem(fila, 2, QStandardItem(m.especie))
            self.model.setItem(fila, 3, QStandardItem(str(m.peso)))

        self.tabla_mascotas.setModel(self.model)

        header = self.tabla_mascotas.horizontalHeader()

        for i in range(self.model.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    def mostrar_grafica(self):

        datos = MascotaService.obtener_especies()

        especies = [d[0] for d in datos]
        cantidades = [d[1] for d in datos]

        plt.bar(especies, cantidades)

        plt.title("Cantidad de mascotas por especie")
        plt.xlabel("Especie")
        plt.ylabel("Cantidad")

        plt.show()

    def pagina_siguiente(self):

        total_paginas = len(self.mascotas) // self.registros_por_pagina + 1

        if self.pagina_actual < total_paginas:
            self.pagina_actual += 1
            self.actualizar_tabla()

    def pagina_anterior(self):

        if self.pagina_actual > 1:
            self.pagina_actual -= 1
            self.actualizar_tabla()

    def filtrar_tabla(self, texto):

        texto = texto.lower()

        for fila in range(self.model.rowCount()):

            nombre = self.model.item(fila, 1).text().lower()
            especie = self.model.item(fila, 2).text().lower()

            visible = texto in nombre or texto in especie

            self.tabla_mascotas.setRowHidden(fila, not visible)

    def on_double_click(self, index):

        id_mascota = self.tabla_mascotas.model().item(
            index.row(), 0
        ).text()

        if self.callback_editar:
            self.callback_editar(int(id_mascota))