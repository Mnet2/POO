from datetime import date

class Proyecto:
    def __init__(self, id_proy=None, nombre="", descripcion="", fecha_inicio=None, director_id=None):
        self._id = id_proy
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._director_id = director_id
        # Lista para almacenar los objetos Empleado que participan
        self._participantes = [] 

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self._fecha_inicio = value

    @property
    def director_id(self):
        return self._director_id
    
    @director_id.setter
    def director_id(self, value):
        self._director_id = value

    @property
    def participantes(self):
        return self._participantes

    def agregar_participante(self, empleado):
        """Agrega un objeto Empleado a la lista local del proyecto."""
        self._participantes.append(empleado)

    def __str__(self):
        return f"Proyecto: {self._nombre} | Inicio: {self._fecha_inicio} | Director ID: {self._director_id}"