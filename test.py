from datetime import date
from Dominio.empleado import Empleado
from Persistencia.empleado_dao import EmpleadoDAO

def probar_insertar_y_listar():
    print("--- INICIANDO PRUEBA DE EMPLEADO ---")

    # 1. Crear un objeto Empleado con datos de prueba
    # Nota: No enviamos ID porque la base de datos lo crea solo
    nuevo_empleado = Empleado(
        nombre="Fabian Test",
        direccion="Calle Python 123",
        telefono="987654321",
        correo="fabian.test@example.com",
        fecha_contrato=date.today(),
        salario=1500000,
        departamento_id=None # Lo dejamos null por ahora
    )

    # 2. Instanciar el DAO
    dao = EmpleadoDAO()

    # 3. Intentar guardar en la Base de Datos
    print(f"Intentando guardar a: {nuevo_empleado.nombre}...")
    exito = dao.agregar(nuevo_empleado)

    if exito:
        print("✅ ¡ÉXITO! Empleado guardado correctamente.")
        print(f"ID generado por la BD: {nuevo_empleado.id}")
    else:
        print("❌ ERROR: No se pudo guardar el empleado.")

    # 4. Leer de la base de datos para confirmar
    print("\n--- LISTADO DE EMPLEADOS EN BD ---")
    todos = dao.mostrar_todos()
    for emp in todos:
        print(emp)

if __name__ == "__main__":
    probar_insertar_y_listar()