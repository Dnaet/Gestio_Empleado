from modelos.empleado import Empleado
from DAL.conexion import ConexionDB

def registrar_empleado_datos(empleado: Empleado):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO empleados (id, nombre, direccion, telefono, email, fecha_inicio, salario, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (empleado.id, empleado.nombre, empleado.direccion, empleado.telefono, empleado.email, empleado.fecha_inicio, empleado.salario, empleado.tipo))
    conexion.connection.commit()
    conexion.desconectar()

def actualizar_empleado_datos(empleado: Empleado):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE empleados SET nombre=%s, direccion=%s, telefono=%s, email=%s, fecha_inicio=%s, salario=%s, tipo=%s WHERE id=%s"
    cursor.execute(sql, (empleado.nombre, empleado.direccion, empleado.telefono, empleado.email, empleado.fecha_inicio, empleado.salario, empleado.tipo, empleado.id))
    conexion.connection.commit()
    conexion.desconectar()

def asignar_departamento_datos(id_empleado: int, departamento_id: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE empleados SET departamento_id=%s WHERE id=%s"
    cursor.execute(sql, (departamento_id, id_empleado))
    conexion.connection.commit()
    conexion.desconectar()

def asignar_proyecto_datos(id_empleado: int, proyecto_id: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO empleados_proyectos (empleado_id, proyecto_id) VALUES (%s, %s)"
    cursor.execute(sql, (id_empleado, proyecto_id))
    conexion.connection.commit()
    conexion.desconectar()