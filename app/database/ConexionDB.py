import pyodbc

class SQL(object):
    __instance   = None
    __session    = None
    __connection = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SQL, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def _open(self):
        try:
            cnx = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=127.0.0.1,1433;Database=datos;Uid=sa;Pwd={1q2w3e4R**};')
            self.__connection = cnx
            self.__session = cnx.cursor()
            print('Connected')
        except pyodbc.Error as err:
            print('Something is wrong...')
            print(err)

    def _close(self):
        try:
            self.__session.close()
            self.__connection.close()
        except Exception as error :
            print(error)

    def call_store_procedure_return(self, name, args):
        try:
            self._open()
            cursor = self.__session
            if args != [] :
                cursor.execute(name, args)
                return cursor.fetchall()
            else:
                cursor.execute(name)
            return cursor.fetchall()
        except Exception as error :
            print(error)

    def execute_procedure(self, name, args):
        try:
            self._open()
            if args != [] :
                self.__session.execute(name, args)
                self.__connection.commit()
            else:
                self.__session.execute(name)
                self.__connection.commit()
                print('Ejecutado')
        except Exception as error :
            print(error)       

cls = SQL()
cls._open()
