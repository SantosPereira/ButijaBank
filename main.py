from data_dao import Client, query
import GUI


print('\n')
print('''\033[1;32m██████╗ ██╗   ██╗████████╗██╗     ██╗ █████╗   ██████╗  █████╗ ███╗  ██╗██╗  ██╗   ██████╗    ██╗ █████╗ \033[0;0m
\033[1;32m██╔══██╗██║   ██║╚══██╔══╝██║     ██║██╔══██╗  ██╔══██╗██╔══██╗████╗ ██║██║ ██╔╝  ██╔════╝   ██╔╝██╔══██╗\033[0;0m
\033[1;32m██████╦╝██║   ██║   ██║   ██║     ██║███████║  ██████╦╝███████║██╔██╗██║█████═╝   ╚█████╗   ██╔╝ ███████║\033[0;0m
\033[1;32m██╔══██╗██║   ██║   ██║   ██║██╗  ██║██╔══██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗    ╚═══██╗ ██╔╝  ██╔══██║\033[0;0m
\033[1;32m██████╦╝╚██████╔╝   ██║   ██║╚█████╔╝██║  ██║  ██████╦╝██║  ██║██║ ╚███║██║ ╚██╗  ██████╔╝██╔╝   ██║  ██║\033[0;0m
\033[1;32m╚═════╝  ╚═════╝    ╚═╝   ╚═╝ ╚════╝ ╚═╝  ╚═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝  ╚═════╝ ╚═╝    ╚═╝  ╚═╝\033[0;0m\n\n\n\n''')

        
def get(): #funcao gatilho e que serve pra chamar as outras passando o parametro adequado #função para acessar dados dos clientes  #y = r ou w  #read ou write
    operação = int(input('''\nQual operação bancária deseja realizar?
Extração de saldo ou depósito?
Para extração de saldo digite [\033[;031m0\033[;0m], para depósito digite [\033[;031m1\033[;0m]
e para acessar o painel de controle digite [\033[;031m9\033[;0m] em seguida a senha de acesso\n\n\n\n>>'''))
    if operação == 0:
        cpf_num = int(input('Digite o número do CPF para a consulta: '))
        Client.le(cpf_num)
       
    elif operação == 1:
        Client.escreve()

    elif operação == 9:
        pwdAccess = int(input('Senha de acesso: '))
        if pwdAccess == 00000:
            print(query('SELECT * FROM main;'))
    else:
        print('Erro! Digite uma opção válida')
        get()

get()
