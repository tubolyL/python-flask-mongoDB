from flask import Flask
from persist.controller import bitcoinapp_api

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(bitcoinapp_api)
    app.run()
