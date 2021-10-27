from typing import List
import mysql.connector

class Banco:
    def __init__(self) -> None:
        self.db_access = mysql.connector.connect(
            host='localhost',
            port='3308',
            user='root',
            database='butija_db'
        )

    def query(self, query) -> List:
        db_cursor = self.db_access.cursor()
        sql = query
        #val = []
        db_cursor.execute(sql)
        data = db_cursor.fetchall()
        self.db_access.commit()
        return data
