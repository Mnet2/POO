class Departamento:
    def __init__(self, id_depto=None, nombre="", gerente_id=None):
        self._id = id_depto
        self._nombre = nombre
        self._gerente_id = gerente_id

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
    def gerente_id(self):
        return self._gerente_id
    
    @gerente_id.setter
    def gerente_id(self, value):
        self._gerente_id = value

    def __str__(self):
        return f"ID: {self._id} | Depto: {self._nombre} | ID Gerente: {self._gerente_id}"