import mysql.connector as mariadb

class Database:
    
    def __init__(self):
        self._mariadb_connection = mariadb.connect(user='root', password='', database='streetweather')
        self._cursor = self._mariadb_connection.cursor()
    
    def set_sql_mode(self):
        self._cursor.execute("SET sql_mode = '' ")
    
    def sql_request(self, query, values):
        self._cursor.execute(query,values)
        self._mariadb_connection.commit()