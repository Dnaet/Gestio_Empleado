import mysql.connector

class ConexionDB:
    def __init__(self):
        self.connection = None

    def conectar(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='gestion_empleados'
        )
        print("Conexión a la base de datos establecida.")

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada.")

    def ejecutar_script_sql(self, archivo_sql):
        try:
            with open(archivo_sql, 'r') as archivo:
                comandos_sql = archivo.read()
            
            cursor = self.connection.cursor()
            for comando in comandos_sql.split(';'):
                comando = comando.strip()
                if comando: 
                    cursor.execute(comando)
                    print(f"Ejecutado: {comando[:50]}...")  

            self.connection.commit()
            print("Todas las tablas se han creado exitosamente.")

        except Exception as e:
            print(f"Error al ejecutar el script SQL: {e}")
        finally:
            cursor.close()

    def crear_tablas_desde_archivo(self, archivo_sql):
        try:
            self.conectar()
            self.ejecutar_script_sql(archivo_sql)
        except mysql.connector.Error as error:
            print(f"Error de conexión a la base de datos: {error}")
        finally:
            self.desconectar()

