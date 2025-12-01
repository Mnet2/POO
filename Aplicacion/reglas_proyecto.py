from Dominio.proyecto import Proyecto
from Persistencia.proyecto_dao import ProyectoDAO
from datetime import datetime

class ReglasProyecto:
    def __init__(self):
        self.dao = ProyectoDAO()

    def crear_proyecto(self, nombre, descripcion, fecha_inicio, director_id):
        # 1. Validaciones
        if not nombre:
            return False, "El proyecto debe tener un nombre."
        
        if not director_id:
            return False, "El proyecto debe tener un director asignado."

        # 2. Crear objeto
        nuevo_proy = Proyecto(
            nombre=nombre, 
            descripcion=descripcion, 
            fecha_inicio=fecha_inicio, 
            director_id=director_id
        )

        # 3. Guardar
        if self.dao.agregar(nuevo_proy):
            return True, f"Proyecto '{nombre}' creado con éxito."
        else:
            return False, "Error al guardar el proyecto."

    def agregar_participante(self, id_proyecto, id_empleado):
        """Conecta un empleado a un proyecto."""
        if self.dao.asignar_participante(id_proyecto, id_empleado):
            return True, "Empleado asignado correctamente al proyecto."
        else:
            return False, "No se pudo asignar (¿Ya estaba asignado o ID incorrecto?)."

    def obtener_todos(self):
        return self.dao.mostrar_todos()