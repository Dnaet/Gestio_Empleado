from modelos.proyecto import Proyecto
from DAL.conexion import ConexionDB

def crear_proyecto_datos(proyecto: Proyecto):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO proyectos (id, nombre, descripcion, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (proyecto.id, proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin))
    conexion.connection.commit()
    conexion.desconectar()

def actualizar_proyecto_datos(proyecto: Proyecto):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE proyectos SET nombre=%s, descripcion=%s, fecha_inicio=%s, fecha_fin=%s WHERE id=%s"
    cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin, proyecto.id))
    conexion.connection.commit()
    conexion.desconectar()

def eliminar_proyecto_datos(id_proyecto: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "DELETE FROM proyectos WHERE id=%s"
    cursor.execute(sql, (id_proyecto,))
    conexion.connection.commit()
    conexion.desconectar()

def informacion_proyecto_datos(id_proyecto: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM proyectos WHERE id=%s"
    cursor.execute(sql, (id_proyecto,))
    proyecto = cursor.fetchone()
    conexion.desconectar()
    return proyecto
