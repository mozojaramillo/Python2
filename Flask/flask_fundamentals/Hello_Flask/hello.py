from flask import Flask, render_template # Importar Flask para que permita crear nuestra aplicacióncopy
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return render_template('index.html')  # Retorna la cadena 'Hello World!' como respuesta



if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depurac