import mysql.connector


class Conexaodb:
    _conn = None
    _host = 'localhost'
    _user = 'root'
    _password = ''
    _db = 'crudescola2022'

    @staticmethod
    def conectar():
        if not Conexaodb._conn:
            try:
                Conexaodb._conn = mysql.connector.connect(
                    host=Conexaodb._host,
                    database=Conexaodb._db,
                    user=Conexaodb._user,
                    password=Conexaodb._password
                )
                return Conexaodb._conn
            except Exception as erro:
                return None
        return Conexaodb._conn

    @staticmethod
    def executarSql(sql, dados=''):
        Conexaodb.conectar()
        try:
            cursor = Conexaodb._conn.cursor(prepared=True)
            cursor.execute(sql,dados)
            Conexaodb._conn.commit()
            return cursor.rowcount
        except Exception as e:
            return e

