from data_dao import Client, query
import GUI

msg = {
    'ajuda':'''\nQual operação bancária deseja realizar?\nExtração de saldo ou depósito?''',
    'msg_input':'''Para extração de saldo digite [\033[;031m0\033[;0m], para depósito digite [\033[;031m1\033[;0m]\ne para acessar o painel de controle digite [\033[;031m9\033[;0m] em seguida a senha de acesso\n\n\n\n\033[;035m>> \033[;0m\033[;034m'''
}

print('\n')
print('''\033[1;32m██████╗ ██╗   ██╗████████╗██╗     ██╗ █████╗   ██████╗  █████╗ ███╗  ██╗██╗  ██╗   ██████╗    ██╗ █████╗ \033[0;0m
\033[1;32m██╔══██╗██║   ██║╚══██╔══╝██║     ██║██╔══██╗  ██╔══██╗██╔══██╗████╗ ██║██║ ██╔╝  ██╔════╝   ██╔╝██╔══██╗\033[0;0m
\033[1;32m██████╦╝██║   ██║   ██║   ██║     ██║███████║  ██████╦╝███████║██╔██╗██║█████═╝   ╚█████╗   ██╔╝ ███████║\033[0;0m
\033[1;32m██╔══██╗██║   ██║   ██║   ██║██╗  ██║██╔══██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗    ╚═══██╗ ██╔╝  ██╔══██║\033[0;0m
\033[1;32m██████╦╝╚██████╔╝   ██║   ██║╚█████╔╝██║  ██║  ██████╦╝██║  ██║██║ ╚███║██║ ╚██╗  ██████╔╝██╔╝   ██║  ██║\033[0;0m
\033[1;32m╚═════╝  ╚═════╝    ╚═╝   ╚═╝ ╚════╝ ╚═╝  ╚═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝  ╚═════╝ ╚═╝    ╚═╝  ╚═╝\033[0;0m\n\n\n\n''')

print(msg['ajuda'])

def get(): #funcao gatilho e que serve pra chamar as outras passando o parametro adequado #função para acessar dados dos clientes  #y = r ou w  #read ou write
    operação = int(input(msg['msg_input']))
    print('\033[;0m')
    if operação == 0:
        cpf_num = int(input('Digite o número do CPF para a consulta: \033[;034m'))
        print('\033[;0m')
        Client.le(cpf_num)

    elif operação == 1:
        try:
            Client.escreve()
        except:
            print('\n\033[;31mDados inseridos já existem no sistema.\nInsira os dados refenrêntes a sua conta.\033[;0m\n\n')
    elif operação == 9:
        pwdAccess = int(input('Senha de acesso: \033[;034m'))
        print('\033[;0m')
        if pwdAccess == 00000:
            data = query('SELECT * FROM main;')
            print('Nome',' '*65,'CPF',' '*16,'Saldo')
            for i in range(len(data)):
                # print(f'\033[;035m{data[i]}\033[;035m')
                str(data[i]).split(',')
                print(f'\033[;036m{data[i][0]}\033[;0m','-'*(70-len(data[i][0])),end='')
                print(f'\033[;036m{data[i][1]}\033[;0m','-'*(20-len(str(data[i][1]))),end='')
                print(f'\033[;036m{data[i][2]}\033[;0m','-'*(10-len(str(data[i][2]))))

    else:
        print('Erro! Digite uma opção válida')
        get()

get()
