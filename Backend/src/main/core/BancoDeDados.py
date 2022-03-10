import mysql.connector

class BancoDeDados:
    def __init__(self) -> None:
        self.db_access = mysql.connector.connect(
            host='localhost',
            port='3308',
            user='root',
            database='butija_db'
        )
