from Presentacion.menu_base import MenuBase
from Presentacion.utilidades import leer_entero, leer_texto
from Aplicacion.reglas_empleado import ReglasEmpleado
from datetime import datetime

class MenuEmpleado(MenuBase):
    def __init__(self):
        super().__init__("Gestión de Empleados")
        self.reglas = ReglasEmpleado()

    def mostrar_opciones(self):
        print("1. Registrar nuevo empleado")
        print("2. Listar todos los empleados")
        print("3. Buscar empleado por ID")
        print("4. Eliminar empleado")
        print("0. Volver al menú principal")

    def procesar_opcion(self, opcion):
        if opcion == 1:
            self.registrar_empleado()
        elif opcion == 2:
            self.listar_empleados()
        elif opcion == 3:
            self.buscar_empleado()
        elif opcion == 4:
            self.eliminar_empleado()
        else:
            print("Opción no válida.")

    def registrar_empleado(self):
        print("\n--- Nuevo Empleado ---")
        
        # 1. Nombre 
        nombre = leer_texto("Nombre: ", 3)
        
        # 2. Dirección y Teléfono
        direccion = leer_texto("Dirección: ")
        
        while True:
            telefono = input("Teléfono (9 dígitos): ").strip()
            if telefono.isdigit() and len(telefono) == 9:
                break
            print("❌ Error: El teléfono debe contener exactamente 9 números (ej: 912345678).")
        
        # 3. Correo 
        while True:
            correo = input("Correo: ").strip()
            if "@" in correo and "." in correo: 
                break
            print("❌ Error: El correo debe contener '@' y un punto (ej: usuario@mail.com). Intente de nuevo.")

        # 4. Salario 
        while True:
            salario = leer_entero("Salario: ")
            if salario >= 0:
                break
            print("❌ Error: El salario no puede ser negativo.")
        
        # 5. Fecha 
        while True:
            fecha_str = input("Fecha Contrato (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha_str, '%Y-%m-%d')
                break 
            except ValueError:
                print("❌ Error: Formato incorrecto. Use Año-Mes-Dia (ej: 2023-10-25).")

        # 6. ID Departamento
        depto_id = leer_entero("ID del Departamento (0 si no tiene): ")
        if depto_id == 0: depto_id = None

        
        exito, mensaje = self.reglas.crear_empleado(
            nombre, direccion, telefono, correo, fecha_str, salario, depto_id
        )
        
        if exito:
            print(f"✅ {mensaje}")
        else:
            print(f"❌ {mensaje}")

    def listar_empleados(self):
        print("\n--- Lista de Empleados ---")
        empleados = self.reglas.obtener_todos()
        if not empleados:
            print("No hay empleados registrados.")
        else:
            print(f"{'ID':<5} | {'Nombre':<20} | {'Correo':<25} | {'Salario':<10}")
            print("-" * 70)
            for emp in empleados:
                print(f"{emp.id:<5} | {emp.nombre:<20} | {emp.correo:<25} | ${emp.salario:<10}")

    def buscar_empleado(self):
        id_emp = leer_entero("Ingrese ID del empleado: ")
        empleado = self.reglas.buscar_por_id(id_emp)
        if empleado:
            print("\n✅ Empleado Encontrado:")
            print(empleado) 
        else:
            print("❌ Empleado no encontrado.")

    def eliminar_empleado(self):
        id_emp = leer_entero("Ingrese ID del empleado a eliminar: ")
        confirmar = leer_texto("¿Está seguro? (s/n): ").lower()
        
        if confirmar == 's':
            exito, msj = self.reglas.eliminar_empleado(id_emp)
            print(msj)
        else:
            print("Operación cancelada.")
            
            