from modelos.usuario import Usuario
from DAL.conexion import ConexionDB

def autenticar_datos(username: str, password: str):
    pass

def cambiar_password_datos(id_usuario: int, nuevo_password: str):
    pass

def asignar_rol_datos(id_usuario: int, rol_id: int):
    pass

def crear_usuario_datos(usuario: Usuario):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "INSERT INTO usuarios (id, nombre, email, password, rol_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (usuario.id, usuario.nombre, usuario.email, usuario.password, usuario.rol.id))
    conexion.connection.commit()
    conexion.desconectar()

def actualizar_usuario_datos(usuario: Usuario):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "UPDATE usuarios SET nombre=%s, email=%s, password=%s, rol_id=%s WHERE id=%s"
    cursor.execute(sql, (usuario.nombre, usuario.email, usuario.password, usuario.rol.id, usuario.id))
    conexion.connection.commit()
    conexion.desconectar()

def eliminar_usuario_datos(id_usuario: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "DELETE FROM usuarios WHERE id=%s"
    cursor.execute(sql, (id_usuario,))
    conexion.connection.commit()
    conexion.desconectar()

def informacion_usuario_datos(id_usuario: int):
    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    sql = "SELECT * FROM usuarios WHERE id=%s"
    cursor.execute(sql, (id_usuario,))
    usuario = cursor.fetchone()
    conexion.desconectar()
    return usuario
