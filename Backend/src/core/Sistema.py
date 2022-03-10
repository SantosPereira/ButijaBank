from Cliente import Cliente
from Conta import *
from util import messages
import os

class Validador:
    def __init__(self) -> None:
        pass

    def valida_entrada(self, nome=None, cpf=None, saldo=None):
        valido = bool # Por padrão começa False
        if nome != None:
            pass
            '''if ... :
                    valido = True 
            '''

        if cpf != None:
            pass
            '''if ... :
                    valido = True 
            '''
        
        if saldo != None:
            pass
            '''if ... :
                    valido = True 
            '''
            
        return valido

    


class Transacoes:
    def __init__(self) -> None:
        pass

    def transferencia_bancaria(conta_pagador, conta_receptador) -> dict: # Objetos do tipo conta_corrente ou conta_poupanca
        pass

    def transferencia_pix() -> dict:
        pass


class Usuario(Cliente):
    def __init__(self) -> None:
        super().__init__