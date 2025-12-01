from Persistencia.conexion import Conexion
from Dominio.departamento import Departamento

class DepartamentoDAO:
    def agregar(self, departamento):
        sql = "INSERT INTO departamentos (nombre, gerente_id) VALUES (%s, %s)"
        val = (departamento.nombre, departamento.gerente_id)
        
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, val)
                conn.commit()
                if cursor.lastrowid:
                    departamento.id = cursor.lastrowid
                return True
            except Exception as e:
                print(f"Error al agregar departamento: {e}")
                return False
            finally:
                conexion_obj.desconectar()
        return False

    def mostrar_todos(self):
        sql = "SELECT * FROM departamentos"
        lista = []
        
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                registros = cursor.fetchall()
                for fila in registros:
                    depto = Departamento(fila[0], fila[1], fila[2])
                    lista.append(depto)
            except Exception as e:
                print(f"Error al listar departamentos: {e}")
            finally:
                conexion_obj.desconectar()
        return lista
        
    def eliminar(self, id_depto):
        sql = "DELETE FROM departamentos WHERE id = %s"
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (id_depto,))
                conn.commit()
                return cursor.rowcount > 0
            except Exception as e:
                print(f"Error al eliminar departamento: {e}")
                return False
            finally:
                conexion_obj.desconectar()
        return False