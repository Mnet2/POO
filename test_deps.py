import random
from Dominio.departamento import Departamento
from Persistencia.departamento_dao import DepartamentoDAO
from Dominio.empleado import Empleado
from Persistencia.empleado_dao import EmpleadoDAO
from datetime import date

def probar_relacion():
    print("\n=== INICIANDO PRUEBA DE INTEGRACIÓN (DEPTO + EMPLEADO) ===")

    # 1. Crear y Guardar el DEPARTAMENTO primero
    # (Necesitamos que exista para que el empleado tenga donde entrar)
    nuevo_depto = Departamento(nombre="Innovación y Desarrollo")
    dao_depto = DepartamentoDAO()

    if dao_depto.agregar(nuevo_depto):
        print(f"✅ Departamento creado: {nuevo_depto.nombre} (ID: {nuevo_depto.id})")
    else:
        print("❌ Error al crear departamento")
        return # Si falla esto, no seguimos

    # 2. Crear el EMPLEADO asignado a ese Departamento
    # Usamos un correo aleatorio para no tener error de "Duplicado" si corres el test varias veces
    correo_random = f"dev{random.randint(1000, 9999)}@ecotech.com"
    
    nuevo_empleado = Empleado(
        nombre="Laura Ingeniera",
        direccion="Av. Tecnológica 500",
        telefono="999888777",
        correo=correo_random,
        fecha_contrato=date.today(),
        salario=1800000,
        departamento_id=nuevo_depto.id  # <--- AQUÍ ESTÁ LA MAGIA: Conectamos con el ID del depto creado arriba
    )

    dao_empleado = EmpleadoDAO()

    if dao_empleado.agregar(nuevo_empleado):
        print(f"✅ Empleado creado: {nuevo_empleado.nombre}")
        print(f"   -> Asignado al Depto ID: {nuevo_empleado.departamento_id}")
    else:
        print("❌ Error al crear empleado")

    # 3. Listar para confirmar visualmente
    print("\n--- RESUMEN EN BASE DE DATOS ---")
    print(f"Departamentos existentes: {len(dao_depto.mostrar_todos())}")
    print(f"Empleados existentes: {len(dao_empleado.mostrar_todos())}")

if __name__ == "__main__":
    probar_relacion()