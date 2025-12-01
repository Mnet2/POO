from datetime import date
from Dominio.proyecto import Proyecto
from Persistencia.proyecto_dao import ProyectoDAO
from Persistencia.empleado_dao import EmpleadoDAO

def probar_proyecto():
    print("\n=== PRUEBA DE PROYECTOS Y PARTICIPANTES ===")
    
    # 1. Crear DAO
    dao_proy = ProyectoDAO()
    dao_emp = EmpleadoDAO() # Necesitamos empleados existentes

    # 2. Crear Proyecto
    nuevo_proy = Proyecto(
        nombre="Sistema EcoTech v1", 
        descripcion="Desarrollo del sistema de gestión", 
        fecha_inicio=date.today(),
        director_id=1 # Asumimos que el empleado con ID 1 existe (el gerente que creamos antes)
    )

    if dao_proy.agregar(nuevo_proy):
        print(f"✅ Proyecto creado: {nuevo_proy.nombre} (ID: {nuevo_proy.id})")
    
        # 3. Asignar participantes (Usamos ID 1 y el ID del empleado que creaste en el test anterior)
        # Asegúrate de tener empleados con estos IDs en tu BD, si no, fallará.
        print("Asignando participantes...")
        dao_proy.asignar_participante(nuevo_proy.id, 1) # Asignamos al empleado 1
        
        # 4. Verificar quienes están
        participantes = dao_proy.obtener_participantes(nuevo_proy.id)
        print(f"👥 El proyecto tiene {len(participantes)} participantes:")
        for p in participantes:
            print(f" - {p.nombre} ({p.correo})")
            
    else:
        print("❌ Error al crear proyecto")

if __name__ == "__main__":
    probar_proyecto()