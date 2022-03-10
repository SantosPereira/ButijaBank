from flask import Flask
from flask_restful import Api
from controller.ClienteController import ClienteController
from controller.ContaController import ContaController

app = Flask(__name__)
api = Api(app)

api.add_Resource(ClienteController, '/cliente/')
api.add_Resource(ContaController, '/conta/')

if __name__ == '__main__':
    app.run()
