from modelos.rol import Rol
from DAL.conexion import ConexionDB

def crear_rol_datos(rol: Rol):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO roles (id, nombre) VALUES (%s, %s)"
    cursor.execute(sql, (rol.id, rol.nombre))
    conexion.connection.commit()
    conexion.desconectar()

def actualizar_rol_datos(rol: Rol):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE roles SET nombre=%s WHERE id=%s"
    cursor.execute(sql, (rol.nombre, rol.id))
    conexion.connection.commit()
    conexion.desconectar()

def eliminar_rol_datos(id_rol: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "DELETE FROM roles WHERE id=%s"
    cursor.execute(sql, (id_rol,))
    conexion.connection.commit()
    conexion.desconectar()

def informacion_rol_datos(id_rol: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM roles WHERE id=%s"
    cursor.execute(sql, (id_rol,))
    rol = cursor.fetchone()
    conexion.desconectar()
    return rol
