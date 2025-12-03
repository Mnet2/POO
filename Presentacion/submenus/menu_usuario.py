from Presentacion.utilidades import limpiar_pantalla, leer_entero
from Aplicacion.reglas_usuario import ReglasUsuario

class MenuUsuario:
    def __init__(self):
        self.reglas = ReglasUsuario()

    def ejecutar(self):
        while True:
            limpiar_pantalla()
            print("="*40)
            print("      GESTIÓN DE USUARIOS (ADMIN)      ")
            print("="*40)
            print("1. Listar Usuarios")
            print("2. Crear Nuevo Usuario")
            print("3. Eliminar Usuario")
            print("0. Volver al Menú Principal")
            print("="*40)
            
            opcion = leer_entero("Seleccione una opción: ")

            if opcion == 1:
                usuarios = self.reglas.listar_usuarios()
                print("\n--- LISTA DE USUARIOS ---")
                print(f"{'Usuario':<15} | {'Rol':<10}")
                print("-" * 30)
                for u in usuarios:
                    print(f"{u['username']:<15} | {u['rol']:<10}")
                input("\nPresione Enter para continuar...")

            elif opcion == 2:
                print("\n--- CREAR USUARIO ---")
                username = input("Nuevo Username: ")
                password = input("Nueva Contraseña: ")
                rol = input("Rol (admin/empleado): ").lower()
                
                if self.reglas.crear_usuario(username, password, rol):
                    print("✅ Usuario creado con éxito.")
                else:
                    print("❌ Error: El usuario ya existe o datos inválidos.")
                input("Enter para continuar...")

            elif opcion == 3:
                print("\n--- ELIMINAR USUARIO ---")
                username = input("Ingrese el username a eliminar: ")
                if username == "admin":
                    print("⛔ No puedes eliminar al administrador principal.")
                elif self.reglas.eliminar_usuario(username):
                    print("✅ Usuario eliminado.")
                else:
                    print("❌ Usuario no encontrado.")
                input("Enter para continuar...")

            elif opcion == 0:
                break