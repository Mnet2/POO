from Presentacion.menu_base import MenuBase
from Presentacion.utilidades import leer_entero, leer_texto
from Aplicacion.reglas_usuario import ReglasUsuario

class MenuUsuario(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Usuarios (Admin)")
        self.reglas = ReglasUsuario()

    def mostrar_opciones(self):
        print("1. Listar Usuarios")
        print("2. Crear Nuevo Usuario")
        print("3. Eliminar Usuario")
        print("4. Editar Usuario") # <--- NUEVA OPCIÓN
        print("0. Volver al Menú Principal")

    def procesar_opcion(self, opcion):
        if opcion == 1:
            self.listar_usuarios()
        elif opcion == 2:
            self.crear_usuario()
        elif opcion == 3:
            self.eliminar_usuario()
        elif opcion == 4:
            self.editar_usuario() # <--- LLAMADA
        else:
            print("Opción no válida.")

    # ... (Tus métodos de listar, crear y eliminar siguen igual) ...

    def editar_usuario(self):
        print("\n--- Editar Usuario ---")
        username = leer_texto("Ingrese el Username del usuario a editar: ")
        
        # Verificamos visualmente si existe antes de pedir datos
        # (Esto es opcional, pero ayuda a la experiencia de usuario)
        if not self.reglas.dao.buscar_por_username(username):
             print("❌ El usuario no existe.")
             return

        print("Deje el campo vacío y presione ENTER si no desea cambiar el valor.")
        
        nueva_pass = input("Nueva Contraseña (vacío para mantener la actual): ")
        nuevo_rol = input("Nuevo Rol (admin/user) (vacío para mantener): ").lower()

        confirmar = leer_texto("¿Guardar cambios? (s/n): ").lower()
        if confirmar == 's':
            exito, mensaje = self.reglas.editar_usuario(username, nueva_pass, nuevo_rol)
            if exito:
                print(f"✅ {mensaje}")
            else:
                print(f"❌ {mensaje}")
        else:
            print("Operación cancelada.")