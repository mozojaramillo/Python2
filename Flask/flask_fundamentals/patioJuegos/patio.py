from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def cuadritos():
    return render_template('index.html', times = 3, color = "blue")

@app.route('/play/<veces>')
def cuadritosmas(veces):
    return render_template('index.html', times = int(veces),color = "blue")

@app.route('/play/<veces>/<color>')
def cuadritosmascolor(veces, color):
    return render_template('index.html', times = int(veces), color = color)


if __name__=="__main__":  
    app.run(debug=True)
