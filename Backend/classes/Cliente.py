from model.data_dao import Banco
from util import messages
import os

class Cliente():
    def __init__(self) -> None:
        self.banco = Banco()
    
    
    def ler(self, cpf):
        data = self.banco.query(f'SELECT nome, cpf, saldo FROM main WHERE cpf={cpf};')
        data = str(data).split(',')
        print('Nome',' '*65,'CPF',' '*20,'Saldo')
        print(f'\033[;036m{data[0]}\033[;0m','-'*(70-len(data[0])),end='')
        print(f'\033[;036m{data[1]}\033[;0m','-'*(20-len(str(data[1]))),end='')
        print('-'*(12-len(str(data[2]))),f'\033[;036m{data[2]}\033[;0m')


    def cadastrar(self, nome, cpf, saldo) -> None:
        try:
            self.banco.query(f'INSERT INTO main (nome, cpf, saldo) VALUES ("{nome}",{cpf},{saldo})')
            print('\n\033[1;32mRegistro inserido com sucesso!!\033[;0m\n\n\n')
            if input():
                try:
                    os.system('cls')
                except:
                    os.system('clear')

        except ValueError:
            print(f'\n\033[1;31mFalha ao inserir registro.\n({ValueError})\033[;0m\nTente novamente\n\n')
            try:
                os.system('cls')
            except:
                os.system('clear')
