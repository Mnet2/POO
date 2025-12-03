import requests
from datetime import datetime

class ServicioAPI:
    def __init__(self):
        self.url = "https://mindicador.cl/api"

    def obtener_indicadores(self):
        """
        Consume una API REST externa (GET) para obtener valor del Dólar, UF y Euro.
        Retorna un diccionario simplificado o None si falla.
        """
        try:
           
            respuesta = requests.get(self.url, timeout=5)
            
            if respuesta.status_code == 200:
                data = respuesta.json()
                
                
                fecha_raw = data['fecha'] 
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
            
            print(f"Error de conexión con la API externa: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado procesando datos: {e}")
            return None