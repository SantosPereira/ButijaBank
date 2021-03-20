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

class Client():
    def le(cpf_num):
        data = query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf_num};')
        data = str(data).split(',')
        print('Nome',' '*65,'CPF',' '*16,'Saldo')
        print(f'\033[;036m{data[0]}\033[;0m','-'*(70-len(data[0])),end='')
        print(f'\033[;036m{data[1]}\033[;0m','-'*(20-len(str(data[1]))),end='')
        print(f'\033[;036m{data[2]}\033[;0m','-'*(10-len(str(data[2]))))
        # print(f'\033[;035m{data}\033[;0m')

    def escreve():
        nome = input('Nome do cliente: \033[;034m')
        cpf = int(input('\033[;0mDigite o CPF do cliente (apenas números): \033[;034m'))
        saldo = float(input('\033[;0mValor de depósito: \033[;034mR$'))
        print('\033[;0m')
        try:
            query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
            print('\n\033[1;32mRegistro inserido com sucesso!!\033[;0m\n\n\n')
            if input():
                import main
        except ValueError:
            print(f'\n\033[1;31mFalha ao inserir registro.\n({ValueError})\033[;0m\nTente novamente\n\n')
            Client.escreve()
