from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QMessageBox, QHeaderView)
from PyQt6.QtCore import Qt
from src.controllers.usuario_controller import UsuarioController
from src.models.usuario import Usuario


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios")
        self.setGeometry(100, 100, 800, 600)
        self.controller = UsuarioController()

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QHBoxLayout(central_widget)

        # Setup UI
        self.setup_form(layout)
        self.setup_table(layout)
        self.cargar_usuarios()

    def setup_form(self, parent_layout):
        form_layout = QVBoxLayout()

        # Campos del formulario
        self.id_input = QLineEdit()
        self.id_input.setVisible(False)

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.telefono_label = QLabel("Teléfono:")
        self.telefono_input = QLineEdit()

        # Añadir campos al layout
        form_layout.addWidget(self.id_input)
        form_layout.addWidget(self.nombre_label)
        form_layout.addWidget(self.nombre_input)
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.telefono_label)
        form_layout.addWidget(self.telefono_input)

        # Botones
        button_layout = QHBoxLayout()

        self.guardar_btn = QPushButton("Guardar")
        self.guardar_btn.clicked.connect(self.guardar_usuario)

        self.limpiar_btn = QPushButton("Limpiar")
        self.limpiar_btn.clicked.connect(self.limpiar_formulario)

        self.eliminar_btn = QPushButton("Eliminar")
        self.eliminar_btn.clicked.connect(self.eliminar_usuario)
        self.eliminar_btn.setVisible(False)

        button_layout.addWidget(self.guardar_btn)
        button_layout.addWidget(self.limpiar_btn)
        button_layout.addWidget(self.eliminar_btn)

        form_layout.addLayout(button_layout)
        form_layout.addStretch()

        parent_layout.addLayout(form_layout)

    def setup_table(self, parent_layout):
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Email", "Teléfono"])
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.table.itemClicked.connect(self.seleccionar_usuario)

        parent_layout.addWidget(self.table)

    def cargar_usuarios(self):
        usuarios = self.controller.obtener_usuarios()
        self.table.setRowCount(len(usuarios))

        for i, usuario in enumerate(usuarios):
            self.table.setItem(i, 0, QTableWidgetItem(str(usuario.id)))
            self.table.setItem(i, 1, QTableWidgetItem(usuario.nombre))
            self.table.setItem(i, 2, QTableWidgetItem(usuario.email))
            self.table.setItem(i, 3, QTableWidgetItem(usuario.telefono))

    def guardar_usuario(self):
        usuario = Usuario(
            id=self.id_input.text() if self.id_input.text() else None,
            nombre=self.nombre_input.text(),
            email=self.email_input.text(),
            telefono=self.telefono_input.text()
        )

        if usuario.id:
            exito = self.controller.actualizar_usuario(usuario)
            mensaje = "Usuario actualizado con éxito!" if exito else "Error al actualizar usuario"
        else:
            exito = self.controller.crear_usuario(usuario)
            mensaje = "Usuario creado con éxito!" if exito else "Error al crear usuario"

        if exito:
            self.mostrar_mensaje("Éxito", mensaje)
            self.cargar_usuarios()
            self.limpiar_formulario()
        else:
            self.mostrar_mensaje("Error", mensaje)

    def eliminar_usuario(self):
        if self.id_input.text():
            confirmacion = QMessageBox.question(
                self,
                "Confirmar eliminación",
                "¿Está seguro de que desea eliminar este usuario?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if confirmacion == QMessageBox.StandardButton.Yes:
                exito = self.controller.eliminar_usuario(self.id_input.text())
                if exito:
                    self.mostrar_mensaje("Éxito", "Usuario eliminado con éxito!")
                    self.cargar_usuarios()
                    self.limpiar_formulario()
                else:
                    self.mostrar_mensaje("Error", "Error al eliminar usuario")

    def seleccionar_usuario(self, item):
        row = item.row()
        self.id_input.setText(self.table.item(row, 0).text())
        self.nombre_input.setText(self.table.item(row, 1).text())
        self.email_input.setText(self.table.item(row, 2).text())
        self.telefono_input.setText(self.table.item(row, 3).text())
        self.eliminar_btn.setVisible(True)

    def limpiar_formulario(self):
        self.id_input.clear()
        self.nombre_input.clear()
        self.email_input.clear()
        self.telefono_input.clear()
        self.eliminar_btn.setVisible(False)

    def mostrar_mensaje(self, titulo, mensaje):
        QMessageBox.information(self, titulo, mensaje)