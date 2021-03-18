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
    data = db_cursor.fetchall()
    db_access.commit()
    return data

class Client(): #objeto cliente --> parâmetros r = read, w = write, a = para adicionar dados ao arquivo
    def le(cpf_num):
        data = query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf_num};')
        print(data)

    def escreve():
        nome = input('Nome do cliente: ')
        cpf = int(input('Digite o CPF do cliente (apenas números): '))
        saldo = float(input('Valor de depósito: R$'))
        try:
            query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
            print('\n\033[1;32mRegistro inserido com sucesso!!\033[;0m\n\n\n')
        except:
            print('\n\033[1;31mFalha ao inserir registro.\033[;0m\nTente novamente\n\n')
            Client.escreve()
