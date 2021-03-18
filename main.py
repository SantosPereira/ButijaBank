import data_dao as sql
import GUI


print('\n')
print('''\033[1;32m██████╗░██╗░░░██╗████████╗██╗░░░░░██╗░█████╗░  ██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░██████╗░░░░██╗░█████╗░\033[0;0m
\033[1;32m██╔══██╗██║░░░██║╚══██╔══╝██║░░░░░██║██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔════╝░░░██╔╝██╔══██╗\033[0;0m
\033[1;32m██████╦╝██║░░░██║░░░██║░░░██║░░░░░██║███████║  ██████╦╝███████║██╔██╗██║█████═╝░  ╚█████╗░░░██╔╝░███████║\033[0;0m
\033[1;32m██╔══██╗██║░░░██║░░░██║░░░██║██╗░░██║██╔══██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░  ░╚═══██╗░██╔╝░░██╔══██║\033[0;0m
\033[1;32m██████╦╝╚██████╔╝░░░██║░░░██║╚█████╔╝██║░░██║  ██████╦╝██║░░██║██║░╚███║██║░╚██╗  ██████╔╝██╔╝░░░██║░░██║\033[0;0m
\033[1;32m╚═════╝░░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░╚═╝░░╚═╝\033[0;0m\n\n\n\n''')

# GUI.janela('Qualquer coisa\nSomente para teste!')
# open("ClientData.txt",'a', encoding="utf8")





def Client_request(y): #função para acessar dados dos clientes  #y = r ou w  #read ou write
    if y == 'r':
        x = int(input('Número do CPF para a consulta: '))
        doc = str(open("ClientData.txt", 'r'))
        x = doc.find(str(x))
        print(x)
        Client.Nome('r',x)
        Client.CPF('r',x)
        Client.Saldo('r',x)
       
    if y == 'w':
        Client.Nome('w',0)
        Client.CPF('w',0)
        Client.Saldo('w',0)

def fsemnome(): #funcao sem nome e que serve pra chamar as outras passando o parametro adequado
    operação = int(input('\nQual operação bancária deseja realizar?\nExtração de saldo ou depósito?\nPara extração de saldo digite [0], para depósito digite [1]\ne para acessar o painel de controle digite [9] em seguida a senha de acesso\n\n\n\n>>'))
    print('\n')
    if operação == 0:
        Client_request('r')

    elif operação == 1:
        Client_request('w')

    elif operação == 9:
        pwAcess = int(input('Senha de acesso: '))
        if pwAcess == 00000:
            doc = open("ClientData.txt",'r', encoding="utf8")
            print(doc.readlines())

    else:
        print('Erro! Digite uma opção válida')
        fsemnome()

fsemnome()


# print(sql.query.rowcount, 'registros Inseridos\n\n\n')
