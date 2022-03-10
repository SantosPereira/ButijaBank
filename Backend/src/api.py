from flask import Flask
from flask_restful import Api
from controller.SistemaController import SistemaController

app = Flask(__name__)
api = Api(app)

api.add_Resource(ControllerAlgumaCoisa, '/')

if __name__ == '__main__':
    app.run()
