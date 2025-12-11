import requests
from datetime import datetime

class ServicioAPI:
    def __init__(self):
        self.url = "https://mindicador.cl/api"

    def obtener_indicadores(self):
        """
        Consume una API REST externa. 
        Si falla por conexión o tiempo de espera, retorna DATOS SIMULADOS 
        para asegurar que el sistema no se detenga.
        """
        try:
            # Aumentamos el timeout a 10 segundos para dar más tiempo
            respuesta = requests.get(self.url, timeout=10)
            
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
                print(f"⚠️ API respondió con código {respuesta.status_code}. Usando respaldo.")
                return self._datos_simulados()

        except requests.exceptions.Timeout:
            print("⚠️ Tiempo de espera agotado (Timeout). Usando datos simulados...")
            return self._datos_simulados()

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error de conexión con la API: {e}. Usando datos simulados...")
            return self._datos_simulados()

        except Exception as e:
            print(f"⚠️ Error inesperado: {e}. Usando datos simulados...")
            return self._datos_simulados()

    def _datos_simulados(self):
        """
        Genera valores fijos de respaldo.
        Esto salva la presentación si no hay internet.
        """
        fecha_hoy = datetime.now().strftime("%d-%m-%Y")
        return {
            "fecha": f"{fecha_hoy} (Offline)",
            "dolar": 985.50, # Valor aproximado realista
            "uf": 36600.00,
            "euro": 1050.20
        }