import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_entero(mensaje):
    """Pide un número hasta que el usuario ingrese uno válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Debe ingresar un número entero válido.")

def leer_texto(mensaje, longitud_minima=1):
    """Pide un texto y valida que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) >= longitud_minima:
            return texto
        print(f"❌ Error: El texto debe tener al menos {longitud_minima} caracteres.")