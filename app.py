from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/ruta')
def ruta1():
    return 'nueva ruta!'


if __name__ == '__main__':
    app.run()
