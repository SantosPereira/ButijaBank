from .BancoDeDados import BancoDeDados

class ConsultaBancoDeDados(BancoDeDados):
    def __init__(self):
        super().__init__()
        
    def query(self, query) -> list:
        db_cursor = self.db_access.cursor()
        sql = query
        #val = []
        db_cursor.execute(sql)
        data = db_cursor.fetchall()
        self.db_access.commit()
        return data
