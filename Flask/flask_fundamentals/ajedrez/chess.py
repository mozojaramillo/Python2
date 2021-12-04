from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ajedrez():
    var1 = 8
    var2 = 8
    return render_template('index.html', var1 = int(var1), var2 = int(var2))