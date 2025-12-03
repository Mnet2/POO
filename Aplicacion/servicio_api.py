import requests
from datetime import datetime

class ServicioAPI:
    def __init__(self):
        # URL de la API gratuita de indicadores económicos de Chile
        self.url = "https://mindicador.cl/api"

    def obtener_indicadores(self):
        """
        Consume una API REST externa (GET) para obtener valor del Dólar, UF y Euro.
        Retorna un diccionario simplificado o None si falla.
        """
        try:
            # Hacemos la petición GET (Time out de 5 seg para que no se congele si no hay net)
            respuesta = requests.get(self.url, timeout=5)
            
            if respuesta.status_code == 200:
                data = respuesta.json()
                
                # Extraemos solo lo que necesitamos y formateamos la fecha
                fecha_raw = data['fecha'] # Viene como '2023-11-01T00:00:00.000Z'
                fecha_bonita = datetime.strptime(fecha_raw[:10], "%Y-%m-%d").strftime("%d-%m-%Y")

                indicadores = {
                    "fecha": fecha_bonita,
                    "dolar": data['dolar']['valor'],
                    "uf": data['uf']['valor'],
                    "euro": data['euro']['valor']
                }
                return indicadores
            else:
                print(f"Error en API: Código {respuesta.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            # Captura errores de conexión (sin internet, timeout, etc.)
            print(f"Error de conexión con la API externa: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado procesando datos: {e}")
            return None