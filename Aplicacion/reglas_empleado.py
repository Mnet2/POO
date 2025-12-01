from Dominio.empleado import Empleado
from Persistencia.empleado_dao import EmpleadoDAO

class ReglasEmpleado:
    def __init__(self):
        self.dao = EmpleadoDAO()

    def crear_empleado(self, nombre, direccion, telefono, correo, fecha_contrato, salario, departamento_id):
        """
        Valida los datos y, si todo está bien, crea el objeto y llama al DAO.
        Retorna: (Exito: bool, Mensaje: str)
        """
        # 1. Validaciones de Reglas de Negocio
        if not nombre or len(nombre) < 3:
            return False, "El nombre debe tener al menos 3 caracteres."
        
        if not correo or "@" not in correo:
            return False, "El correo electrónico no es válido."
            
        if salario < 0:
            return False, "El salario no puede ser negativo."

        # 2. Crear el objeto Empleado
        nuevo_empleado = Empleado(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            fecha_contrato=fecha_contrato,
            salario=salario,
            departamento_id=departamento_id
        )

        # 3. Llamar a la capa de persistencia
        if self.dao.agregar(nuevo_empleado):
            return True, f"Empleado {nombre} registrado con éxito (ID: {nuevo_empleado.id})."
        else:
            return False, "Error en la base de datos al intentar guardar."

    def obtener_todos(self):
        """Retorna la lista completa de empleados."""
        return self.dao.mostrar_todos()

    def buscar_por_id(self, id_empleado):
        """Busca un empleado, validando que el ID sea un número válido."""
        try:
            id_num = int(id_empleado)
            return self.dao.buscar_por_id(id_num)
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return None

    def eliminar_empleado(self, id_empleado):
        """Elimina un empleado, verificando antes si existe."""
        if self.buscar_por_id(id_empleado):
            if self.dao.eliminar(id_empleado):
                return True, "Empleado eliminado correctamente."
            else:
                return False, "Error al intentar eliminar en la BD."
        else:
            return False, "El empleado no existe."