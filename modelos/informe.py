from modelos.empleado import Empleado as empleado_id
from modelos.departamento import Departamento as departamento_id
from modelos.proyecto import Proyecto as proyecto_id



class Informe:
    def __init__(self, id, titulo, contenido):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido


