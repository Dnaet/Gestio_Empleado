from modelos.empleado import Empleado
from modelos.proyecto import Proyecto
from modelos.informe import Informe
from modelos.usuario import Usuario
from modelos.departamento import Departamento
from modelos.rol import Rol
from modelos.registro_tiempo import RegistroDeTiempo

from datos.empleado_datos import EmpleadoDatos
from datos.proyecto_datos import ProyectoDatos
from datos.informe_datos import InformeDatos
from datos.usuario_datos import UsuarioDatos
from datos.departamento_datos import DepartamentoDatos
from datos.rol_datos import RolDatos
from datos.registro_tiempo_datos import RegistroDeTiempoDatos

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN ===")
    print("1. Gestionar Empleados")
    print("2. Gestionar Proyectos")
    print("3. Generar Informes")
    print("4. Gestionar Usuarios")
    print("5. Gestionar Departamentos")
    print("6. Gestionar Roles")
    print("7. Registrar Tiempo")
    print("8. Salir")
    return input("Seleccione una opción: ")

def menu_empleados():
    print("\n--- GESTIÓN DE EMPLEADOS ---")
    print("1. Registrar nuevo empleado")
    print("2. Actualizar empleado")
    print("3. Asignar empleado a un departamento")
    print("4. Asignar empleado a un proyecto")
    print("5. Volver al menú principal")
    return input("Seleccione una opción: ")

def gestionar_empleados():
    empleado_datos = EmpleadoDatos()
    while True:
        opcion = menu_empleados()
        if opcion == "1":
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            salario = float(input("Salario: "))
            tipo = input("Tipo (Administrador/Empleado Regular): ")
            
            nuevo_empleado = Empleado(None, nombre, direccion, telefono, email, fecha_inicio, salario, tipo)
            empleado_datos.registrar_empleado_datos(nuevo_empleado)
            print("Empleado registrado correctamente.")
        elif opcion == "2":
            # Actualización de empleado
            id_empleado = int(input("ID del empleado: "))
            nombre = input("Nuevo nombre: ")
            direccion = input("Nueva dirección: ")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
            salario = float(input("Nuevo salario: "))
            tipo = input("Nuevo tipo (Administrador/Empleado Regular): ")
            
            empleado_actualizado = Empleado(id_empleado, nombre, direccion, telefono, email, fecha_inicio, salario, tipo)
            empleado_datos.actualizar_empleado_datos(empleado_actualizado)
            print("Empleado actualizado correctamente.")
        elif opcion == "3":
            # Asignar departamento
            id_empleado = int(input("ID del empleado: "))
            id_departamento = int(input("ID del departamento: "))
            empleado_datos.asignar_departamento_datos(id_empleado, id_departamento)
            print("Departamento asignado correctamente.")
        elif opcion == "4":
            # Asignar proyecto
            id_empleado = int(input("ID del empleado: "))
            id_proyecto = int(input("ID del proyecto: "))
            empleado_datos.asignar_proyecto_datos(id_empleado, id_proyecto)
            print("Proyecto asignado correctamente.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            gestionar_empleados()
        elif opcion == "2":
            print("Funcionalidad para gestionar proyectos próximamente.")
        elif opcion == "3":
            print("Funcionalidad para generar informes próximamente.")
        elif opcion == "4":
            print("Funcionalidad para gestionar usuarios próximamente.")
        elif opcion == "5":
            print("Funcionalidad para gestionar departamentos próximamente.")
        elif opcion == "6":
            print("Funcionalidad para gestionar roles próximamente.")
        elif opcion == "7":
            print("Funcionalidad para registrar tiempo próximamente.")
        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
