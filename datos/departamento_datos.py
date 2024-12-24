from modelos.departamento import Departamento
from DAL.conexion import ConexionDB

def crear_departamento_datos(departamento: Departamento):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO departamentos (id, nombre, gerente) VALUES (%s, %s, %s)"
    cursor.execute(sql, (departamento.id, departamento.nombre, departamento.gerente))
    conexion.connection.commit()
    conexion.desconectar()

def editar_departamento_datos(departamento: Departamento):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE departamentos SET nombre=%s, gerente=%s WHERE id=%s"
    cursor.execute(sql, (departamento.nombre, departamento.gerente, departamento.id))
    conexion.connection.commit()
    conexion.desconectar()

def eliminar_departamento_datos(id_departamento: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "DELETE FROM departamentos WHERE id=%s"
    cursor.execute(sql, (id_departamento,))
    conexion.connection.commit()
    conexion.desconectar()

def informacion_departamento_datos(id_departamento: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM departamentos WHERE id=%s"
    cursor.execute(sql, (id_departamento,))
    departamento = cursor.fetchone()
    conexion.desconectar()
    return departamento