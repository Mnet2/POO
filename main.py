import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Presentacion.utilidades import limpiar_pantalla, leer_entero
from Presentacion.submenus.menu_empleado import MenuEmpleado
from Presentacion.submenus.menu_departamento import MenuDepartamento
from Presentacion.submenus.menu_proyecto import MenuProyecto

def main():
    while True:
        limpiar_pantalla()
        print("="*40)
        print("      SISTEMA ECOTECH SOLUTIONS      ")
        print("="*40)
        print("1. Gestión de Empleados")
        print("2. Gestión de Departamentos") 
        print("3. Gestión de Proyectos")
        print("0. Salir")
        print("="*40)

        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            menu = MenuEmpleado()
            menu.ejecutar()
            
        elif opcion == 2:
            menu = MenuDepartamento()
            menu.ejecutar()
            
        elif opcion == 3:
            menu = MenuProyecto()
            menu.ejecutar()

        elif opcion == 0:
            print("\n¡Hasta luego! Cerrando sistema...")
            break
        else:
            print("\n❌ Opción inválida.")
            input("Presione ENTER para intentar de nuevo...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSalida forzada por el usuario.")