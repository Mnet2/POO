from Presentacion.menu_base import MenuBase
from Presentacion.utilidades import leer_entero, leer_texto, limpiar_pantalla
from Aplicacion.reglas_usuario import ReglasUsuario
import getpass

class MenuUsuario(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Usuarios (Admin)")
        self.reglas = ReglasUsuario()

    def mostrar_opciones(self):
        print("1. Listar Usuarios")
        print("2. Crear Nuevo Usuario")
        print("3. Eliminar Usuario")
        print("4. Editar Usuario") 
        print("0. Volver al Menú Principal")

    def procesar_opcion(self, opcion):
        if opcion == 1:
            self.listar_usuarios()
        elif opcion == 2:
            self.crear_usuario()
        elif opcion == 3:
            self.eliminar_usuario()
        elif opcion == 4:
            self.editar_usuario()
        else:
            print("Opción no válida.")

    # --- IMPLEMENTACIÓN DE LOS MÉTODOS QUE FALTABAN ---

    def listar_usuarios(self):
        print("\n--- Lista de Usuarios ---")
        usuarios = self.reglas.listar_usuarios()
        
        if not usuarios:
            print("No hay usuarios registrados (o error de conexión).")
        else:
            print(f"{'Usuario':<20} | {'Rol':<10}")
            print("-" * 35)
            # Como el DAO devuelve una lista de diccionarios {'username':..., 'rol':...}
            for u in usuarios:
                print(f"{u['username']:<20} | {u['rol']:<10}")

    def crear_usuario(self):
        print("\n--- Crear Nuevo Usuario ---")
        username = leer_texto("Username: ")
        
        # Validación simple de contraseña
        while True:
            password = input("Password: ")
            if len(password) > 0:
                break
            print("La contraseña no puede estar vacía.")

        rol = ""
        while rol not in ['admin', 'user']:
            rol = input("Rol (admin/user): ").lower()
        
        exito = self.reglas.crear_usuario(username, password, rol)
        
        if exito:
            print(f"✅ Usuario '{username}' creado exitosamente.")
        else:
            print("❌ No se pudo crear el usuario (Tal vez ya existe).")

    def eliminar_usuario(self):
        print("\n--- Eliminar Usuario ---")
        username = leer_texto("Username a eliminar: ")
        
        if username == 'admin':
            print("❌ No se puede eliminar al administrador principal por seguridad.")
            return

        confirmar = leer_texto("¿Está seguro? (s/n): ").lower()
        if confirmar == 's':
            if self.reglas.eliminar_usuario(username):
                print("✅ Usuario eliminado correctamente.")
            else:
                print("❌ Error al eliminar (Usuario no existe o error de BD).")
        else:
            print("Operación cancelada.")

    def editar_usuario(self):
        print("\n--- Editar Usuario ---")
        username = leer_texto("Ingrese el Username del usuario a editar: ")
        
        # Verificamos visualmente si existe antes de pedir datos
        if not self.reglas.dao.buscar_por_username(username):
             print("❌ El usuario no existe.")
             return

        print("Deje el campo vacío y presione ENTER si no desea cambiar el valor.")
        
        nueva_pass = input("Nueva Contraseña (vacío para mantener la actual): ")
        nuevo_rol = input("Nuevo Rol (admin/user) (vacío para mantener): ").lower()

        if not nueva_pass and not nuevo_rol:
            print("No se realizaron cambios.")
            return

        confirmar = leer_texto("¿Guardar cambios? (s/n): ").lower()
        if confirmar == 's':
            exito, mensaje = self.reglas.editar_usuario(username, nueva_pass, nuevo_rol)
            if exito:
                print(f"✅ {mensaje}")
            else:
                print(f"❌ {mensaje}")
        else:
            print("Operación cancelada.")