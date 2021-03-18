import data_dao as sql


class Client(): #objeto cliente --> parâmetros r = read, w = write, a = para adicionar dados ao arquivo
    def le(cpf_num):
        sql.query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf_num};')

    def escreve():
        nome = input('Nome do cliente: ')
        cpf = int(input('Digite o CPF do cliente (apenas números): '))
        saldo = float(input('Valor de depósito: R$'))

        sql.query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
