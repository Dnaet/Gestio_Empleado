from modelos.empleado import Empleado as empleado_id
from modelos.proyecto import Proyecto as proyecto_id

 

class RegistroDeTiempo(proyecto_id, empleado_id):
    def __init__(self, id_registro, fecha, horas_trabajadas, descripcion, empleado_id, proyecto_id):
        self.id_registro = id_registro
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id
