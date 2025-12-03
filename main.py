import sys
import os
import threading  # <--- NUEVO: Para ejecutar la API en paralelo
import uvicorn    # <--- NUEVO: Servidor para la API
from fastapi import FastAPI # <--- NUEVO: Framework de API
from pydantic import BaseModel # <--- NUEVO: Validación de datos
from dotenv import load_dotenv

# Cargar variables del archivo .env antes de cualquier cosa
load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Presentacion.utilidades import limpiar_pantalla, leer_entero
from Presentacion.submenus.menu_empleado import MenuEmpleado
from Presentacion.submenus.menu_departamento import MenuDepartamento
from Presentacion.submenus.menu_proyecto import MenuProyecto
from Presentacion.login import iniciar_sesion 
from Aplicacion.reglas_usuario import ReglasUsuario
from Aplicacion.servicio_api import ServicioAPI 
from Presentacion.submenus.menu_usuario import MenuUsuario 

# ==============================================================================
# 1. BLOQUE NUEVO: CONFIGURACIÓN DE TU API (FASTAPI)
# ==============================================================================
app = FastAPI()

class Item(BaseModel):
    nombre: str
    precio: float
    en_oferta: bool = False

@app.get("/")
def read_root():
    return {"sistema": "EcoTech Solutions", "estado": "Online"}

@app.post("/items/")
def create_item(item: Item):
    return {"nombre_recibido": item.nombre, "precio_recibido": item.precio}

def arrancar_api():
    # log_level="critical" evita que la API ensucie tu consola con textos mientras usas el menú
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="critical")

# ==============================================================================
# 2. TU LÓGICA DE MENÚ ORIGINAL
# ==============================================================================
def main():
    # --- SEMILLA: Crear usuario Admin ---
    try:
        reglas_usr = ReglasUsuario()
        reglas_usr.crear_usuario_inicial("admin", "1234", "admin")
    except Exception as e:
        print(f"Nota: Verificando integridad de usuarios... ({e})")

    # --- LOGIN ---
    usuario_actual = iniciar_sesion()

    if not usuario_actual:
        return 

    # --- MENÚ PRINCIPAL ---
    while True:
        limpiar_pantalla()
        print("="*40)
        print("      SISTEMA ECOTECH SOLUTIONS      ")
        print("      (API Web corriendo en puerto 8000)      ") # Aviso visual
        print("="*40)
        print(f"👤 Usuario: {usuario_actual.username} | 🔑 Rol: {usuario_actual.rol.upper()}")
        print("-" * 40)
        
        print("1. Gestión de Empleados")
        print("2. Gestión de Departamentos") 
        print("3. Gestión de Proyectos")
        print("4. Gestión de Usuarios (Admin)") 
        print("5. Indicadores Económicos (API Externa)")
        
        print("0. Salir")
        print("="*40)

        opcion = leer_entero("Seleccione una opción: ")

        if opcion == 1:
            MenuEmpleado().ejecutar() 
        elif opcion == 2:
            MenuDepartamento().ejecutar()
        elif opcion == 3:
            MenuProyecto().ejecutar()
        elif opcion == 4:
            if usuario_actual.rol == 'admin':
                MenuUsuario().ejecutar() 
                input("Enter para continuar...")
            else:
                print("\n⛔ ACCESO DENEGADO")
                input("Enter para continuar...")
        elif opcion == 5:
            print("\nconectando con API externa...")
            api = ServicioAPI()
            datos = api.obtener_indicadores()
            if datos:
                print("\n--- 💰 INDICADORES ECONÓMICOS ---")
                print(f"📅 Fecha: {datos['fecha']}")
                print(f"🇺🇸 Dólar: ${datos['dolar']}")
                print(f"🏠 UF:    ${datos['uf']}")
                print(f"🇪🇺 Euro:  ${datos['euro']}")
            else:
                print("❌ Error de conexión.")
            input("\nEnter para volver...")

        elif opcion == 0:
            print("\n¡Hasta luego! Cerrando sistema...")
            break
        else:
            print("\n❌ Opción inválida.")
            input("Enter...")

# ==============================================================================
# 3. EJECUCIÓN (HILOS + MAIN)
# ==============================================================================
if __name__ == "__main__":
    try:
        # A. INICIAMOS LA API EN UN HILO SEPARADO (DAEMON)
        # Daemon significa que si cierras el programa principal, la API se apaga sola.
        hilo_api = threading.Thread(target=arrancar_api, daemon=True)
        hilo_api.start()
        print(">>> API Web iniciada correctamente en segundo plano...")

        # B. INICIAMOS TU SISTEMA DE MENÚS
        main()
        
    except KeyboardInterrupt:
        print("\n\nSalida forzada por el usuario.")