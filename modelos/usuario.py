from modelos.rol import Rol

class Usuario:
    def __init__(self, id, nombre, email, password, rol: Rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.rol = rol
