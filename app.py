from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'THANK YOU BABE!\nWant to tell you I have finished my projects with udacity.\nI am very gratefull to God for giving me the priviledge to meet you, what a beautiful person you are.\nI love you, I love you\n'



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
