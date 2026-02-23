from flask import Flask, render_template, request
from models.recomendacao import Recomendacao
from models.database import init_db

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/listadesejo', methods=['GET', 'POST'])
def listadesejo():
    recomendacoes = None

    if request.method == 'POST':
        titulo_recomendacao = request.form ['titulo-recomendacao']
        quem_recomendacao = request.form['quem-recomendacao']
        tipo_recomendacao = request.form['tipo-recomendacao']
        recomendacao = Recomendacao(titulo_recomendacao, quem_recomendacao, tipo_recomendacao) 
        recomendacao.salvar_recomendacao()

    recomendacoes = Recomendacao.obter_recomendacoes()

    return render_template('ListaDesejo.html', titulo= 'Before Letter Box', recomendacoes=recomendacoes)