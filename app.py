from flask import Flask, redirect, render_template, request, url_for
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

    return render_template('ListaDesejo.html', titulo= 'Before', recomendacoes=recomendacoes)


@app.route('/delete/<int:idRecomendacao>')
def delete(idRecomendacao):
    recomendacao = Recomendacao.id(idRecomendacao)
    recomendacao.excluir_recomendacao()
    return redirect(url_for('listadesejo'))

@app.route('/update/<int:idRecomendacao>' , methods=['GET', 'POST'])
def update(idRecomendacao):

    if request.method == 'POST':
        titulo = request.form ['titulo-recomendacao']
        quem = request.form['quem-recomendacao']
        tipo = request.form['tipo-recomendacao']
        recomendacao = Recomendacao(titulo, quem, tipo, idRecomendacao) 
        recomendacao.atualizar_recomendacao()
        return redirect(url_for('listadesejo'))
    
    recomendacoes = Recomendacao.obter_recomendacoes()
    recomendacao_selecionada = Recomendacao.id(idRecomendacao)

    return render_template('listadesejo.html', titulo= 'Lista de Desejos', recomendacoes=recomendacoes, recomendacao_selecionada=recomendacao_selecionada)