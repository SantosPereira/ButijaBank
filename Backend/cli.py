import os
from time import sleep

from util import messages
from model.data_dao import Banco
from classes.Cliente import Cliente


def run():
    banco = Banco()
    cliente = Cliente()

    try:
        os.system('cls')
    except:
        os.system('clear')

    print('\n')
    print(messages.logo)
    print(messages.msg['ajuda'])
    

    operação = int(input(messages.msg['msg_input']))
    print('\033[;0m')
    if operação == 0:
        cpf = int(input('Digite o número do CPF para a consulta: \033[;034m'))
        print('\033[;0m')
        cliente.ler(cpf)

    elif operação == 1:
        try:
            nome = input('Nome do cliente: \033[;034m')
            cpf = int(input('\033[;0mDigite o CPF do cliente (apenas números): \033[;034m'))
            saldo = float(input('\033[;0mValor de depósito: \033[;034mR$'))
            print('\033[;0m')
            cliente.cadastrar(nome, cpf, saldo)
        except:
            print('\n\033[;31mDados inseridos já existem no sistema.\nInsira os dados refenrêntes a sua conta.\033[;0m\n\n')
            sleep(5)
            try:
                os.system('cls')
            except:
                os.system('clear')
            run()
    elif operação == 9:
        pwdAccess = int(input('Senha de acesso: \033[;034m'))
        print('\033[;0m')
        if pwdAccess == 00000:
            data = banco.query('SELECT * FROM main;')
            print('Nome',' '*65,'CPF',' '*16,'Saldo')
            for i in range(len(data)):
                # print(f'\033[;035m{data[i]}\033[;035m')
                str(data[i]).split(',')
                print(f'\033[;036m{data[i][0]}\033[;0m','-'*(70-len(data[i][0])),end='')
                print(f'\033[;036m{data[i][1]}\033[;0m','-'*(20-len(str(data[i][1]))),end='')
                print(f'\033[;036m{data[i][2]}\033[;0m','-'*(10-len(str(data[i][2]))))

    else:
        print('Erro! Digite uma opção válida')
        sleep(5)
        try:
            os.system('cls')
        except:
            os.system('clear')
        run()
