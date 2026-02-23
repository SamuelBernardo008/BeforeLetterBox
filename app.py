from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/listadesejo', methods=['GET', 'POST'])
def listadesejo():
    return render_template('ListaDesejo.html', titulo= 'Lista de Desejos')