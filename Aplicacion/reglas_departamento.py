from Dominio.departamento import Departamento
from Persistencia.departamento_dao import DepartamentoDAO

class ReglasDepartamento:
    def __init__(self):
        self.dao = DepartamentoDAO()

    def crear_departamento(self, nombre, gerente_id=None):
        # 1. Validar reglas
        if not nombre or len(nombre) < 2:
            return False, "El nombre del departamento es muy corto."

        # 2. Crear objeto
        nuevo_depto = Departamento(nombre=nombre, gerente_id=gerente_id)

        # 3. Guardar
        if self.dao.agregar(nuevo_depto):
            return True, f"Departamento '{nombre}' creado (ID: {nuevo_depto.id})."
        else:
            return False, "Error al guardar el departamento."

    def obtener_todos(self):
        return self.dao.mostrar_todos()

    def eliminar_departamento(self, id_depto):
        if self.dao.eliminar(id_depto):
            return True, "Departamento eliminado."
        else:
            return False, "No se pudo eliminar (verifique si existe)."