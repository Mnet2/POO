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
    
    # ... (Mantén tus métodos buscar_por_username y agregar igual que antes) ...

    def listar_todos(self):
        """Devuelve una lista de diccionarios o objetos Usuario."""
        sql = "SELECT username, rol FROM usuarios"
        conexion = Conexion()
        conn = conexion.conectar()
        lista = []
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                registros = cursor.fetchall()
                for fila in registros:
                    # Devolvemos un dict o un objeto parcial para listar
                    lista.append({"username": fila[0], "rol": fila[1]})
            except Exception as e:
                print(f"Error al listar usuarios: {e}")
            finally:
                conexion.desconectar()
        return lista

    def eliminar(self, username):
        """Elimina un usuario de la BD."""
        sql = "DELETE FROM usuarios WHERE username = %s"
        conexion = Conexion()
        conn = conexion.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (username,))
                conn.commit()
                return cursor.rowcount > 0
            except Exception as e:
                print(f"Error al eliminar usuario: {e}")
                return False
            finally:
                conexion.desconectar()
        return False
    
    def actualizar(self, usuario, password_hash):
        """
        Actualiza el rol y la contraseña (hash) de un usuario existente.
        """
        sql = "UPDATE usuarios SET password = %s, rol = %s WHERE username = %s"
        conexion = Conexion()
        conn = conexion.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                # Nota: El WHERE username es el último parámetro
                cursor.execute(sql, (password_hash, usuario.rol, usuario.username))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al actualizar usuario: {e}")
                return False
            finally:
                conexion.desconectar()
        return False