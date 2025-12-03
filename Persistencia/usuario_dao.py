from Persistencia.conexion import Conexion
from Dominio.usuario import Usuario

class UsuarioDAO:
    def buscar_por_username(self, username):
        """Busca un usuario por su nombre de usuario."""
        sql = "SELECT * FROM usuarios WHERE username = %s"
        conexion = Conexion()
        conn = conexion.conectar()
        resultado = None
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (username,))
                fila = cursor.fetchone()
                if fila:
                  
                    resultado = Usuario(fila[0], fila[1], fila[2], fila[3])
            except Exception as e:
                print(f"Error al buscar usuario: {e}")
            finally:
                conexion.desconectar()
        return resultado

    def agregar(self, usuario, password_hash):
        """Guarda un nuevo usuario con la contraseña YA encriptada."""
        sql = "INSERT INTO usuarios (username, password, rol) VALUES (%s, %s, %s)"
        conexion = Conexion()
        conn = conexion.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (usuario.username, password_hash, usuario.rol))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al crear usuario: {e}")
                return False
            finally:
                conexion.desconectar()
        return False