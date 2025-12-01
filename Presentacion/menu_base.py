from abc import ABC, abstractmethod
from Presentacion.utilidades import limpiar_pantalla, leer_entero

class MenuBase(ABC):
    def __init__(self, nombre_menu):
        self.nombre = nombre_menu

    def mostrar_encabezado(self):
        limpiar_pantalla()
        print("="*40)
        print(f"SISTEMA ECOTECH - {self.nombre.upper()}")
        print("="*40)

    def ejecutar(self):
        while True:
            self.mostrar_encabezado()
            self.mostrar_opciones()
            
            try:
                opcion = leer_entero("\nSeleccione una opción: ")
                if opcion == 0:
                    break
                self.procesar_opcion(opcion)
                input("\nPresione ENTER para continuar...")
            except Exception as e:
                print(f"❌ Ocurrió un error inesperado: {e}")
                input("Presione ENTER para continuar...")

    @abstractmethod
    def mostrar_opciones(self):
        pass

    @abstractmethod
    def procesar_opcion(self, opcion):
        pass