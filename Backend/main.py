from model.data_dao import Banco
from classes import Cliente, Sistema
import cli

# ############################### Modos de execução ############################### #
def cliMode():
    cli.run()

def flask():
    pass

if __name__ == '__main__':
    cliMode()