from Presentacion.menu_base import MenuBase
from Presentacion.utilidades import leer_entero, leer_texto
from Aplicacion.reglas_departamento import ReglasDepartamento

class MenuDepartamento(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Departamentos")
        self.reglas = ReglasDepartamento()

    def mostrar_opciones(self):
        print("1. Crear nuevo departamento")
        print("2. Listar departamentos")
        print("3. Eliminar departamento")
        print("0. Volver al menú principal")

    def procesar_opcion(self, opcion):
        if opcion == 1:
            self.crear_depto()
        elif opcion == 2:
            self.listar_deptos()
        elif opcion == 3:
            self.eliminar_depto()
        else:
            print("Opción no válida.")

    def crear_depto(self):
        print("\n--- Nuevo Departamento ---")
        nombre = leer_texto("Nombre del Departamento: ", 2)
        
        # Opcional: Asignar gerente al crear
        gerente_id = leer_entero("ID del Gerente (0 si no tiene): ")
        if gerente_id == 0: gerente_id = None

        exito, mensaje = self.reglas.crear_departamento(nombre, gerente_id)
        
        if exito:
            print(f"✅ {mensaje}")
        else:
            print(f"❌ {mensaje}")

    def listar_deptos(self):
        print("\n--- Departamentos ---")
        deptos = self.reglas.obtener_todos()
        if not deptos:
            print("No hay departamentos registrados.")
        else:
            print(f"{'ID':<5} | {'Nombre':<30} | {'ID Gerente':<10}")
            print("-" * 50)
            for d in deptos:
                # Manejo de None para gerente_id
                id_gerente = d.gerente_id if d.gerente_id is not None else "Sin asignar"
                print(f"{d.id:<5} | {d.nombre:<30} | {id_gerente:<10}")

    def eliminar_depto(self):
        id_depto = leer_entero("Ingrese ID del departamento a eliminar: ")
        exito, msj = self.reglas.eliminar_departamento(id_depto)
        print(msj)