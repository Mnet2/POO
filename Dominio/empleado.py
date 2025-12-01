from datetime import date

class Empleado:
    def __init__(self, id_emp=None, nombre="", direccion="", telefono="", correo="", fecha_contrato=None, salario=0, departamento_id=None):
        # El ID es None por defecto porque la base de datos lo genera automáticamente
        self._id = id_emp
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._fecha_contrato = fecha_contrato
        self._salario = salario
        self._departamento_id = departamento_id

    # Getters y Setters (Encapsulamiento)
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
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self, value):
        self._correo = value

    @property
    def fecha_contrato(self):
        return self._fecha_contrato
    
    @fecha_contrato.setter
    def fecha_contrato(self, value):
        self._fecha_contrato = value

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, value):
        # Validación básica: el salario no debería ser negativo
        if value >= 0:
            self._salario = value
        else:
            print("Error: El salario no puede ser negativo")

    @property
    def departamento_id(self):
        return self._departamento_id
    
    @departamento_id.setter
    def departamento_id(self, value):
        self._departamento_id = value

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Correo: {self._correo} | Salario: ${self._salario}"