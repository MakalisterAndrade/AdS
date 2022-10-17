import mysql.connector as msqc

class Conexaodb:
    _conn = None
    _host = 'localhost'
    _user = 'root'
    _password = ''
    _bd = 'crudescola2022'

    @staticmethod
    def conectar():
        if Conexaodb._conn == None:
            try:
                Conexaodb._conn = msqc.Connect(
                    host=Conexaodb._host, # 'localhost'
                    database=Conexaodb._bd,
                    user=Conexaodb._user,
                    password=Conexaodb._password,
                )
                return Conexaodb._conn
            except Exception as erro:
                return erro
            return Conexaodb._conn


    @staticmethod
    def executarSql(sql, dados):
        try:
            cursor = Conexaodb._conn.cursor(prepared = True)
            cursor.execute(sql, dados)
            Conexaodb._conn.commit()
            return cursor.rowcount
        except Exception as e:
            return e