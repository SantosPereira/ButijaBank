from core.ConsultaBancoDeDados import ConsultaBancoDeDados as DB

class Dao:
    def __init__(self) -> None:
        self.db = DB()


    def cadastrar(self, nome, cpf, saldo) -> str:
        try:
            self.db.query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
            return f'\n\033[1;32mRegistro inserido com sucesso!!\033[;0m\n\n\n'
        except ValueError:
            return f'\n\033[1;31mFalha ao inserir registro.\n({ValueError})\033[;0m\nTente novamente\n\n'
    

    def ler(self, cpf) -> str:
        data = self.db.query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf};')
        return data
    
    def atualizar(self) -> None:
        pass


    def deletar(self, cpf) -> str:
        try:
            self.db.query(f'DELETE FROM main WHERE cpf={cpf}')
            return 'Registro deletado com sucesso!'
        except:
            return 'Ocorreu um erro, tente novamente.'
