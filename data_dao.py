import mysql.connector

db_access = mysql.connector.connect(
    host='localhost',
    user='root',
    database='butija_db'
)
def query(query):
    db_cursor = db_access.cursor()
    sql = query
    #val = []
    db_cursor.execute(sql)
    db_access.commit()
    return db_cursor.rowcount


class Client(): #objeto cliente --> parâmetros r = read, w = write, a = para adicionar dados ao arquivo
    def le(cpf_num):
        query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf_num};')

    def escreve():
        nome = input('Nome do cliente: ')
        cpf = int(input('Digite o CPF do cliente (apenas números): '))
        saldo = float(input('Valor de depósito: R$'))
        registro = query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
        if registro != 0:
            print('\nRegistro inserido com sucesso!!\n\n\n')
        else:
            print('\nFalha ao inserir registro.\n\nTente novamente\n\n')
            Client.escreve()
        