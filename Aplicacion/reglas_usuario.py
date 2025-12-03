import json
import os
from Dominio.entidades import Usuario 

class ReglasUsuario:
    def __init__(self):
        self.archivo = "usuarios.json"
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                json.dump([], f)

    def _leer_archivo(self):
        with open(self.archivo, 'r') as f:
            return json.load(f)

    def _guardar_archivo(self, datos):
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def crear_usuario_inicial(self, username, password, rol):
        usuarios = self._leer_archivo()
        
        for u in usuarios:
            if u['username'] == username:
                return False
       
        nuevo = {"username": username, "password": password, "rol": rol}
        usuarios.append(nuevo)
        self._guardar_archivo(usuarios)
        return True

    def listar_usuarios(self):
        return self._leer_archivo()

    def crear_usuario(self, username, password, rol):
        usuarios = self._leer_archivo()
        
        if any(u['username'] == username for u in usuarios):
            return False
        
        nuevo = {"username": username, "password": password, "rol": rol}
        usuarios.append(nuevo)
        self._guardar_archivo(usuarios)
        return True

    def eliminar_usuario(self, username):
        usuarios = self._leer_archivo()
        inicial = len(usuarios)
      
        usuarios = [u for u in usuarios if u['username'] != username]
        
        if len(usuarios) < inicial:
            self._guardar_archivo(usuarios)
            return True
        return False
        
    def login(self, username, password):
        usuarios = self._leer_archivo()
        for u in usuarios:
            if u['username'] == username and u['password'] == password:
               
                usuario_encontrado = Usuario(u['username'], u['password'], u['rol'])
                
                return True, "Inicio de sesión exitoso", usuario_encontrado
        
       
        return False, "Usuario o contraseña incorrectos", None