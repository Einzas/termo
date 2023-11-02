import sqlite3


class Database:
    def __init__(self, db_path='./database/database.sqlite3'):
        self.db_path = db_path

    def _connect(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        return conn, cursor

    def _close(self, conn):
        conn.commit()
        conn.close()

    def query(self, value):
        conn, cursor = self._connect()
        cursor.execute(value)
        data = cursor.fetchall()
        self._close(conn)
        return data

    def update(self, value, data):
        conn, cursor = self._connect()
        for i in data:
            cursor.execute(value, i)
        self._close(conn)

    def update_data(self, table, value, where):
        conn, cursor = self._connect()
        sql = f"UPDATE {table} SET {value} WHERE {where}"
        cursor.execute(sql)
        self._close(conn)

    def update_data_params(self, table, value, data, where):
        conn, cursor = self._connect()
        sql = f"UPDATE {table} SET {value} = ? WHERE {where}"
        for i in data:
            cursor.execute(sql, i)
        self._close(conn)

    def info(self, table, value, where=None):
        conn, cursor = self._connect()
        if where:
            sql = f"SELECT {value} FROM {table} WHERE {where}"
        else:
            sql = f"SELECT {value} FROM {table}"
        cursor.execute(sql)
        data = cursor.fetchall()
        self._close(conn)
        return data
