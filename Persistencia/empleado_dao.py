from Persistencia.conexion import Conexion
from Dominio.empleado import Empleado

class EmpleadoDAO:
    def agregar(self, empleado):
        """
        Recibe un objeto Empleado y lo inserta en la base de datos.
        Retorna True si la operación fue exitosa.
        """
        sql = """
            INSERT INTO empleados (nombre, direccion, telefono, correo, fecha_contrato, salario, departamento_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            empleado.nombre, 
            empleado.direccion, 
            empleado.telefono, 
            empleado.correo, 
            empleado.fecha_contrato, 
            empleado.salario,
            empleado.departamento_id
        )
        
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit() 
                
                if cursor.lastrowid:
                    empleado.id = cursor.lastrowid
                    
                return True
            except Exception as e:
                print(f"Error al agregar empleado: {e}")
                return False
            finally:
                conexion_obj.desconectar()
        return False

    def mostrar_todos(self):
        """Devuelve una lista con todos los empleados."""
        sql = "SELECT * FROM empleados"
        lista_empleados = []
        
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                registros = cursor.fetchall()
                
                for fila in registros:
                    emp = Empleado(
                        id_emp=fila[0],
                        nombre=fila[1],
                        direccion=fila[2],
                        telefono=fila[3],
                        correo=fila[4],
                        fecha_contrato=fila[5],
                        salario=fila[6],
                        departamento_id=fila[7]
                    )
                    lista_empleados.append(emp)
            except Exception as e:
                print(f"Error al listar empleados: {e}")
            finally:
                conexion_obj.desconectar()
        
        return lista_empleados

    def buscar_por_id(self, id_empleado):
        """Busca un empleado por su ID."""
        sql = "SELECT * FROM empleados WHERE id = %s"
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        resultado = None
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (id_empleado,))
                fila = cursor.fetchone()
                if fila:
                    resultado = Empleado(
                        id_emp=fila[0], nombre=fila[1], direccion=fila[2],
                        telefono=fila[3], correo=fila[4], fecha_contrato=fila[5],
                        salario=fila[6], departamento_id=fila[7]
                    )
            except Exception as e:
                print(f"Error al buscar empleado: {e}")
            finally:
                conexion_obj.desconectar()
        return resultado

    def eliminar(self, id_empleado):
        """Elimina un empleado por su ID."""
        sql = "DELETE FROM empleados WHERE id = %s"
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        exito = False
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (id_empleado,))
                conn.commit()
                if cursor.rowcount > 0:
                    exito = True
            except Exception as e:
                print(f"Error al eliminar empleado: {e}")
            finally:
                conexion_obj.desconectar()
        return exito