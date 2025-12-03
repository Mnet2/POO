import pymysql
from pymysql import Error

class Conexion:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__db = "ecotech_db"
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__db
            )
            return self.conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def desconectar(self):
        if self.conexion:
            self.conexion.close()