from modelos.registro_tiempo import RegistroDeTiempo
from DAL.conexion import ConexionDB

def registrar_tiempo_datos(registro: RegistroDeTiempo):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO registros_tiempo (id, empleado_id, proyecto_id, horas, fecha) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (registro.id, registro.empleado.id, registro.proyecto.id, registro.horas, registro.fecha))
    conexion.connection.commit()
    conexion.desconectar()

def actualizar_registro_tiempo_datos(registro: RegistroDeTiempo):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE registros_tiempo SET empleado_id=%s, proyecto_id=%s, horas=%s, fecha=%s WHERE id=%s"
    cursor.execute(sql, (registro.empleado.id, registro.proyecto.id, registro.horas, registro.fecha, registro.id))
    conexion.connection.commit()
    conexion.desconectar()

def eliminar_registro_tiempo_datos(id_registro: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "DELETE FROM registros_tiempo WHERE id=%s"
    cursor.execute(sql, (id_registro,))
    conexion.connection.commit()
    conexion.desconectar()

def informacion_registro_tiempo_datos(id_registro: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM registros_tiempo WHERE id=%s"
    cursor.execute(sql, (id_registro,))
    registro = cursor.fetchone()
    conexion.desconectar()
    return registro
