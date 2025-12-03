from Aplicacion.reglas_usuario import ReglasUsuario
from Presentacion.utilidades import limpiar_pantalla, leer_texto
import getpass # Para ocultar la contraseña al escribir (opcional pero recomendado)

def iniciar_sesion():
    reglas = ReglasUsuario()
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        limpiar_pantalla()
        print("="*40)
        print("      SEGURIDAD ECOTECH - LOGIN      ")
        print("="*40)
        print(f"Intento {intentos + 1} de {max_intentos}")

        user = leer_texto("Usuario: ")
        # getpass oculta lo que escribes, si da problemas en VS Code usa input() normal
        try:
            password = getpass.getpass("Contraseña: ")
        except:
            password = input("Contraseña: ")

        exito, mensaje, usuario_obj = reglas.login(user, password)

        if exito:
            print(f"\n✅ {mensaje}")
            input("Presione ENTER para ingresar...")
            return usuario_obj # Retornamos el usuario para saber su rol en el main
        else:
            print(f"\n❌ {mensaje}")
            intentos += 1
            input("Presione ENTER para intentar de nuevo...")

    print("\n⛔ BLOQUEADO: Ha excedido el número de intentos.")
    return None