import os
from time import sleep

from util import mensagens
from util.data_dao import Dao
from core.ConsultaBancoDeDados import ConsultaBancoDeDados as Banco


def run():
    banco = Banco()
    dao = Dao()

    try: os.system('cls')
    except: os.system('clear')

    print('\n'); print(mensagens.logo); print(mensagens.msg['ajuda'])
    operacao = int(input(mensagens.msg['msg_input'])); print('\033[;0m')

    if operacao == 0:
        cpf = int(input('Digite o número do CPF para a consulta: \033[;034m')); print('\033[;0m')
        data = dao.ler(cpf)
        data = str(data).split(',')
        espaco1 = str('-'*(70-len(data[0])))
        espaco2 = str('-'*(20-len(str(data[1]))))
        info = str('Nome'+str(' '*65)+'CPF'+str(' '*20)+'Saldo\n'+f'\033[;036m{data[0]}\033[;0m'+ espaco1 +f'\033[;036m{data[1]}\033[;0m'+ espaco2 + f'\033[;036m{data[2]}\033[;0m')
        print(info)

    elif operacao == 1:
        try:
            nome = input('Nome do cliente: \033[;034m')
            cpf = int(input('\033[;0mDigite o CPF do cliente (apenas números): \033[;034m'))
            saldo = float(input('\033[;0mValor de depósito: \033[;034mR$')); print('\033[;0m')
            
            print(dao.cadastrar(nome, cpf, saldo))
        except:
            print('\n\033[;31mDados inseridos já existem no sistema.\nInsira os dados refenrêntes a sua conta.\033[;0m\n\n')
            sleep(5)
            run()

    elif operacao == 9:
        pwdAccess = int(input('Senha de acesso: \033[;034m')); print('\033[;0m')
        if pwdAccess == 00000:
            operacao = int(input(mensagens.msg['admin'])); print('\033[0;0m')
            if operacao == 0: # Ver registros
                data = banco.query('SELECT * FROM main;')
                print('\n\n')
                print('Nome',' '*65,'CPF',' '*16,'Saldo')
                for i in range(len(data)):
                    str(data[i]).split(',')
                    print(f'\033[;036m{data[i][0]}\033[;0m','-'*(70-len(data[i][0])),end='')
                    print(f'\033[;036m{data[i][1]}\033[;0m','-'*(20-len(str(data[i][1]))),end='')
                    print(f'\033[;036m{data[i][2]}\033[;0m','-'*(10-len(str(data[i][2]))))

    else:
        print('Erro! Digite uma opção válida')
        sleep(5)
        run()


if __name__ == '__main__':
    run()
