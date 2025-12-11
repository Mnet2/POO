import bcrypt
from Persistencia.usuario_dao import UsuarioDAO
from Dominio.usuario import Usuario

class ReglasUsuario:
    def __init__(self):
        self.dao = UsuarioDAO()

    def crear_usuario_inicial(self, username, password, rol):
        """
        Método requerido por main.py para crear el admin al arrancar.
        Solo lo crea si no existe.
        """
        if not self.dao.buscar_por_username(username):
            print(f"--- Creando usuario inicial del sistema: {username} ---")
            self.crear_usuario(username, password, rol)
        else:
            # Si ya existe, no hacemos nada (silencioso)
            pass

    def listar_usuarios(self):
        """Obtiene todos los usuarios desde la Base de Datos."""
        return self.dao.listar_todos()

    def crear_usuario(self, username, password, rol):
        """
        Crea un usuario con contraseña encriptada.
        """
        # 1. Verificar si ya existe
        if self.dao.buscar_por_username(username):
            print(f"Error: El usuario '{username}' ya existe.")
            return False

        # 2. Encriptar contraseña (Bcrypt)
        # hashpw necesita bytes, por eso hacemos encode
        bytes_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes_password, salt)

        # 3. Crear objeto y guardar
        # CORRECCIÓN IMPORTANTE: Usamos argumentos nombrados para evitar mezclar el ID con el Username
        nuevo_usuario = Usuario(
            id_usr=None,  # El ID lo genera la base de datos
            username=username, 
            password=password, # Esto es solo para el objeto en memoria
            rol=rol
        )
        
        # Pasamos el hash real al DAO (decodificado a string para guardarlo en SQL)
        if self.dao.agregar(nuevo_usuario, hashed_password.decode('utf-8')):
            return True
        return False

    def eliminar_usuario(self, username):
        """Elimina un usuario por su nombre de usuario."""
        return self.dao.eliminar(username)

    def login(self, username, password_plana):
        """
        Valida las credenciales comparando el hash de la BD.
        """
        usuario_encontrado = self.dao.buscar_por_username(username)

        if usuario_encontrado:
            # usuario_encontrado.password contiene el HASH que vino de la BD
            hash_guardado = usuario_encontrado.password
            
            # Verificar con bcrypt
            # Convertimos ambos a bytes para la comparación segura
            try:
                if bcrypt.checkpw(password_plana.encode('utf-8'), hash_guardado.encode('utf-8')):
                    return True, "Inicio de sesión exitoso", usuario_encontrado
                else:
                    return False, "Contraseña incorrecta", None
            except ValueError:
                return False, "Error de formato en la contraseña guardada", None
        
        return False, "Usuario no encontrado", None
    
    def editar_usuario(self, username, nueva_pass_plana, nuevo_rol):
        """
        Permite editar contraseña (re-encriptando) y/o rol.
        Si nueva_pass_plana es vacío, se mantiene la contraseña actual.
        """
        # 1. Buscar el usuario actual para no perder datos
        usuario_actual = self.dao.buscar_por_username(username)
        
        if not usuario_actual:
            return False, "El usuario no existe."

        # 2. Lógica de la Contraseña
        hash_final = usuario_actual.password # Por defecto mantenemos la vieja
        
        if nueva_pass_plana and len(nueva_pass_plana.strip()) > 0:
            # Si escribió algo, generamos nuevo hash
            salt = bcrypt.gensalt()
            hash_final = bcrypt.hashpw(nueva_pass_plana.encode('utf-8'), salt).decode('utf-8')
        
        # 3. Lógica del Rol
        if nuevo_rol and len(nuevo_rol.strip()) > 0:
            usuario_actual._rol = nuevo_rol # Actualizamos el objeto (usando el setter interno o directo)

        # 4. Enviar al DAO
        # Pasamos el objeto usuario (que tiene el username y el nuevo rol) y el hash (nuevo o viejo)
        if self.dao.actualizar(usuario_actual, hash_final):
            return True, "Usuario actualizado correctamente."
        else:
            return False, "Error al guardar los cambios en la BD."