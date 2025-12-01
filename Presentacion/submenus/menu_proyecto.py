from Presentacion.menu_base import MenuBase
from Presentacion.utilidades import leer_entero, leer_texto
from Aplicacion.reglas_proyecto import ReglasProyecto
from Aplicacion.reglas_empleado import ReglasEmpleado 
from datetime import datetime

class MenuProyecto(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Proyectos")
        self.reglas = ReglasProyecto()
        self.reglas_empleado = ReglasEmpleado()

    def mostrar_opciones(self):
        print("1. Crear nuevo proyecto")
        print("2. Listar proyectos")
        print("3. Asignar empleado a proyecto (Participante)")
        print("4. Ver participantes de un proyecto")
        print("0. Volver al menú principal")

    def procesar_opcion(self, opcion):
        if opcion == 1:
            self.crear_proyecto()
        elif opcion == 2:
            self.listar_proyectos()
        elif opcion == 3:
            self.asignar_participante()
        elif opcion == 4:
            self.ver_participantes()
        else:
            print("Opción no válida.")

    def crear_proyecto(self):
        print("\n--- Nuevo Proyecto ---")
        nombre = leer_texto("Nombre del Proyecto: ", 3)
        descripcion = leer_texto("Descripción: ")
        
        # Validación de Fecha
        while True:
            fecha_str = input("Fecha Inicio (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha_str, '%Y-%m-%d')
                break
            except ValueError:
                print("❌ Error: Formato incorrecto. Use Año-Mes-Dia.")

        # Validación de Director
        while True:
            director_id = leer_entero("ID del Empleado Director: ")
            if self.reglas_empleado.buscar_por_id(director_id):
                break
            print("❌ Error: Ese empleado no existe. Ingrese un ID válido.")

        exito, mensaje = self.reglas.crear_proyecto(nombre, descripcion, fecha_str, director_id)
        
        if exito:
            print(f"✅ {mensaje}")
        else:
            print(f"❌ {mensaje}")

    def listar_proyectos(self):
        print("\n--- Proyectos Activos ---")
        proyectos = self.reglas.obtener_todos()
        if not proyectos:
            print("No hay proyectos registrados.")
        else:
            print(f"{'ID':<5} | {'Nombre':<20} | {'Inicio':<12} | {'ID Director':<10}")
            print("-" * 55)
            for p in proyectos:
                # CORRECCIÓN: Manejo de valores None (Nulos) para evitar errores
                dir_id = p.director_id if p.director_id is not None else "N/A"
                fecha = str(p.fecha_inicio) if p.fecha_inicio else "N/A"
                
                print(f"{p.id:<5} | {p.nombre:<20} | {fecha:<12} | {dir_id:<10}")

    def asignar_participante(self):
        print("\n--- Asignar Empleado a Proyecto ---")
        id_proy = leer_entero("ID del Proyecto: ")
        id_emp = leer_entero("ID del Empleado a agregar: ")

        exito, msj = self.reglas.agregar_participante(id_proy, id_emp)
        if exito:
            print(f"✅ {msj}")
        else:
            print(f"❌ {msj}")

    def ver_participantes(self):
        print("\n--- Ver Participantes ---")
        id_proy = leer_entero("Ingrese ID del Proyecto: ")
        
        participantes = self.reglas.dao.obtener_participantes(id_proy)
        
        if not participantes:
            print("Este proyecto no tiene participantes asignados o no existe.")
        else:
            print(f"👥 Participantes del Proyecto {id_proy}:")
            for emp in participantes:
                print(f" - {emp.nombre} (ID: {emp.id})")