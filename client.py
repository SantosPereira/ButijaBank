
class Client(): #objeto cliente --> parâmetros r = read, w = write, a = para adicionar dados ao arquivo
    def Nome(r_or_w,x): #self como primeiro parâmetro só seria necessario caso fosse precisar de outro atributo da classe
        if r_or_w == 'r':
            sql.query('SELECT nome FROM main;')
            '''
            doc = open("ClientData.txt", 'r')
            print('Cliente: ',doc.readlines()[x]) #o número entre colchetes é o termo da lista ser buscado
            '''

        elif r_or_w == 'w':
            texto = input('Nome do cliente: ')
            sql.query(f'INSERT INTO main (nome) VALUES ({texto})')
            '''
            doc = open("ClientData.txt", 'a')
            doc.write(f'@{texto}!\n')
            '''

    def CPF(r_or_w,x):
        if r_or_w == 'r':
            sql.query('SELECT cpf FROM main;')
            '''
            doc = open("ClientData.txt", 'r')
            print('CPF: ',doc.readlines()[x]) # comentário na linha 20
            '''

        elif r_or_w == 'w':
            texto = input('Digite o CPF do cliente (apenas números): ')
            sql.query(f'INSERT INTO main (cpf) VALUES ({texto})')
            '''
            doc = open("ClientData.txt", 'a')
            doc.write(f'&{texto}#\n')
            '''

    def Saldo(r_or_w,x):
        if r_or_w == 'r':
            sql.query('SELECT saldo FROM main;')
            '''
            doc = open("ClientData.txt", 'r')
            print('Saldo: ',doc.readlines()[x]) # comentário na linha 20
            '''

        elif r_or_w == 'w':
            texto = input('Valor de depósito: R$')
            sql.query(f'INSERT INTO main (saldo) VALUES ({texto})')
            '''
            print('\n')
            doc = open("ClientData.txt", 'a')
            doc.write(f'${texto}%\n')
            '''
