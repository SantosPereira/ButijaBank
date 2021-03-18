#import csv
#from sys import 

print('\n')
print('''\033[1;32m██████╗░██╗░░░██╗████████╗██╗░░░░░██╗░█████╗░  ██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░██████╗░░░░██╗░█████╗░\033[0;0m
\033[1;32m██╔══██╗██║░░░██║╚══██╔══╝██║░░░░░██║██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔════╝░░░██╔╝██╔══██╗\033[0;0m
\033[1;32m██████╦╝██║░░░██║░░░██║░░░██║░░░░░██║███████║  ██████╦╝███████║██╔██╗██║█████═╝░  ╚█████╗░░░██╔╝░███████║\033[0;0m
\033[1;32m██╔══██╗██║░░░██║░░░██║░░░██║██╗░░██║██╔══██║  ██╔══██╗██╔══██║██║╚████║██╔═██╗░  ░╚═══██╗░██╔╝░░██╔══██║\033[0;0m
\033[1;32m██████╦╝╚██████╔╝░░░██║░░░██║╚█████╔╝██║░░██║  ██████╦╝██║░░██║██║░╚███║██║░╚██╗  ██████╔╝██╔╝░░░██║░░██║\033[0;0m
\033[1;32m╚═════╝░░╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░╚═╝░░╚═╝\033[0;0m\n\n\n\n''')


open("ClientData.txt",'a', encoding="utf8")


class Client(): #objeto cliente --> parâmetros r = read, w = write, a = para adicionar dados ao arquivo
    def Nome(r_or_w,x): #self como primeiro parâmetro só seria necessario caso fosse precisar de outro atributo da classe
        if r_or_w == 'r':
            doc = open("ClientData.txt", 'r')
            print('Cliente: ',doc.readlines()[x]) #o número entre colchetes é o termo da lista ser buscado
            

        elif r_or_w == 'w':
            texto = input('Nome do cliente: ')
            doc = open("ClientData.txt", 'a')
            doc.write(f'@{texto}!\n')

    def CPF(r_or_w,x):
        if r_or_w == 'r':
            doc = open("ClientData.txt", 'r')
            print('CPF: ',doc.readlines()[x]) # comentário na linha 20
         

        elif r_or_w == 'w':
            texto = input('Digite o CPF do cliente (apenas números): ')
            doc = open("ClientData.txt", 'a')
            doc.write(f'&{texto}#\n')

    def Saldo(r_or_w,x):
        if r_or_w == 'r':
            doc = open("ClientData.txt", 'r')
            print('Saldo: ',doc.readlines()[x]) # comentário na linha 20
            

        elif r_or_w == 'w':
            texto = input('Valor de depósito: R$')
            print('\n')
            doc = open("ClientData.txt", 'a')
            doc.write(f'${texto}%\n')




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
    operação = int(input('\nQual operação bancária deseja realizar?\nExtração de saldo ou depósito?\nPara extração de saldo digite [0] e para depósito digite [1]\n\n\n\n>>'))
    print('\n')
    if operação == 0:
        Client_request('r')
    elif operação == 1:
        Client_request('w')
    else:
        print('Erro! Digite uma opção válida')
        fsemnome()

fsemnome()
