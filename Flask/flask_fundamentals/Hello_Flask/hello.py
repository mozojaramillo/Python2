from flask import Flask  # Importar Flask para que permita crear nuestra aplicacióncopy
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return '¡Hola Mundo!'  # Retorna la cadena 'Hello World!' como respuesta

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return f'hello {name}'

@app.route('/repetir/<n>/<name>')
def rep(n, name):
    return f'{name}' *int(n)

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depurac