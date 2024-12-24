from modelos.informe import Informe
from DAL.conexion import ConexionDB

def generar_informe_datos(informe: Informe):

    conexion = ConexionDB()
    conexion.conectar()
    cursor = conexion.connection.cursor()
    
    
    sql = """
    SELECT d.nombre AS departamento, e.nombre AS empleado, e.email, e.telefono
    FROM empleados e
    JOIN departamentos d ON e.departamento_id = d.id
    ORDER BY d.nombre, e.nombre
    """
    
    cursor.execute(sql)
    resultados = cursor.fetchall()
    
    # Procesar los resultados y generar el informe
    informe.contenido = resultados
    
    conexion.desconectar()
    return informe