class Usuario:
    def __init__(self, id=None, nombre="", email="", telefono=""):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono
        }