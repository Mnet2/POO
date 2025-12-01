from Persistencia.conexion import Conexion
from Dominio.proyecto import Proyecto
from Dominio.empleado import Empleado

class ProyectoDAO:
    def agregar(self, proyecto):
        """Guarda un proyecto en la base de datos."""
        sql = "INSERT INTO proyectos (nombre, descripcion, fecha_inicio, director_id) VALUES (%s, %s, %s, %s)"
        val = (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.director_id)
        
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, val)
                conn.commit()
                if cursor.lastrowid:
                    proyecto.id = cursor.lastrowid
                return True
            except Exception as e:
                print(f"Error al agregar proyecto: {e}")
                return False
            finally:
                conexion_obj.desconectar()
        return False

    def mostrar_todos(self):
        """Devuelve una lista de todos los proyectos."""
        sql = "SELECT * FROM proyectos"
        lista = []
        
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql)
                registros = cursor.fetchall()
                for fila in registros:
                    # fila: id, nombre, descripcion, fecha_inicio, director_id
                    proy = Proyecto(fila[0], fila[1], fila[2], fila[3], fila[4])
                    lista.append(proy)
            except Exception as e:
                print(f"Error al listar proyectos: {e}")
            finally:
                conexion_obj.desconectar()
        return lista

    def buscar_por_id(self, id_proyecto):
        """Busca un proyecto y retorna el objeto."""
        sql = "SELECT * FROM proyectos WHERE id = %s"
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        resultado = None
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (id_proyecto,))
                fila = cursor.fetchone()
                if fila:
                    resultado = Proyecto(fila[0], fila[1], fila[2], fila[3], fila[4])
            except Exception as e:
                print(f"Error al buscar proyecto: {e}")
            finally:
                conexion_obj.desconectar()
        return resultado
    
    # --- MÉTODOS ESPECIALES PARA LA RELACIÓN MUCHOS A MUCHOS ---

    def asignar_participante(self, proyecto_id, empleado_id):
        """Agrega un empleado a la lista de participantes de un proyecto."""
        sql = "INSERT INTO proyecto_participantes (proyecto_id, empleado_id) VALUES (%s, %s)"
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (proyecto_id, empleado_id))
                conn.commit()
                return True
            except Exception as e:
                print(f"Error al asignar participante: {e}")
                return False
            finally:
                conexion_obj.desconectar()
        return False

    def obtener_participantes(self, proyecto_id):
        """Devuelve una lista de objetos Empleado que están en un proyecto."""
        # Esta consulta une (JOIN) la tabla intermedia con la tabla empleados
        sql = """
            SELECT e.* FROM empleados e
            INNER JOIN proyecto_participantes pp ON e.id = pp.empleado_id
            WHERE pp.proyecto_id = %s
        """
        lista_participantes = []
        conexion_obj = Conexion()
        conn = conexion_obj.conectar()
        
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (proyecto_id,))
                registros = cursor.fetchall()
                for fila in registros:
                    emp = Empleado(
                        id_emp=fila[0], nombre=fila[1], direccion=fila[2],
                        telefono=fila[3], correo=fila[4], fecha_contrato=fila[5],
                        salario=fila[6], departamento_id=fila[7]
                    )
                    lista_participantes.append(emp)
            except Exception as e:
                print(f"Error al obtener participantes: {e}")
            finally:
                conexion_obj.desconectar()
        return lista_participantes