from src.config.database import DatabaseConnection
from src.models.usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()
        self.cursor = self.connection.cursor()

    def crear_usuario(self, usuario):
        sql = """INSERT INTO usuarios (nombre, email, telefono) 
                 VALUES (%s, %s, %s)"""
        values = (usuario.nombre, usuario.email, usuario.telefono)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error creando usuario: {e}")
            return False

    def obtener_usuarios(self):
        sql = "SELECT * FROM usuarios"
        try:
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            usuarios = []
            for row in resultados:
                usuario = Usuario(row[0], row[1], row[2], row[3])
                usuarios.append(usuario)
            return usuarios
        except Exception as e:
            print(f"Error obteniendo usuarios: {e}")
            return []

    def actualizar_usuario(self, usuario):
        sql = """UPDATE usuarios 
                 SET nombre = %s, email = %s, telefono = %s 
                 WHERE id = %s"""
        values = (usuario.nombre, usuario.email, usuario.telefono, usuario.id)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error actualizando usuario: {e}")
            return False

    def eliminar_usuario(self, id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        try:
            self.cursor.execute(sql, (id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error eliminando usuario: {e}")
            return False
