class Usuario:
    def __init__(self, id_usr=None, username="", password="", rol="user"):
        self._id = id_usr
        self._username = username
        self._password = password
        self._rol = rol

    @property
    def id(self): return self._id
    
    @property
    def username(self): return self._username
    
    @property
    def password(self): return self._password
    
    @property
    def rol(self): return self._rol

    def __str__(self):
        return f"Usuario: {self._username} | Rol: {self._rol}"