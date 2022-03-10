import mysql.connector

class Banco:
    def __init__(self) -> None:
        self.db_access = mysql.connector.connect(
            host='localhost',
            port='3308',
            user='root',
            database='butija_db'
        )

    def query(self, query) -> list:
        db_cursor = self.db_access.cursor()
        sql = query
        #val = []
        db_cursor.execute(sql)
        data = db_cursor.fetchall()
        self.db_access.commit()
        return data

class Dao:
    def __init__(self) -> None:
        self.banco = Banco()


    def cadastrar(self, nome, cpf, saldo) -> str:
        try:
            self.banco.query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
            return f'\n\033[1;32mRegistro inserido com sucesso!!\033[;0m\n\n\n'
        except ValueError:
            return f'\n\033[1;31mFalha ao inserir registro.\n({ValueError})\033[;0m\nTente novamente\n\n'
    

    def ler(self, cpf) -> str:
        data = self.banco.query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf};')
        data = str(data).split(',')
        espaco1 = str('-'*(70-len(data[0])))
        espaco2 = str('-'*(20-len(str(data[1]))))
        return str('Nome'+str(' '*65)+'CPF'+str(' '*20)+'Saldo\n'+f'\033[;036m{data[0]}\033[;0m'+ espaco1 +f'\033[;036m{data[1]}\033[;0m'+ espaco2 + f'\033[;036m{data[2]}\033[;0m')

    
    def atualizar(self) -> None:
        pass


    def deletar(self, cpf) -> str:
        try:
            self.banco.query(f'DELETE FROM main WHERE cpf={cpf}')
            return 'Registro deletado com sucesso!'
        except:
            return 'Ocorreu um erro, tente novamente.'
