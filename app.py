from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.tarefa import Tarefa

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')


@app.route('/ola')
def ola_mundo():
    return "olá, mundo"

@app.route('/BeforeLetterBox', methods=['GET', 'POST'])
def before_letter_box():
    tarefas = None
    
    if request.method == 'POST':
        titulo_tarefa = request.form ['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao) 
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template('BeforeLetterBox.html', titulo= 'Before Letter Box', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('before_letter_box'))

@app.route('/update/<int:idTarefa>' , methods=['GET', 'POST'])
def update(idTarefa):

    if request.method == 'POST':
        titulo = request.form ['titulo-tarefa']
        data = request.form['data-conclusao']
        tarefa = Tarefa(titulo, data, idTarefa) 
        tarefa.atualizar_tarefa()
        return redirect(url_for('before_letter_box'))
    
    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)

    return render_template('BeforeLetterBox.html', titulo= 'BeforeLetterBox', tarefas=tarefas, tarefa_selecionada=tarefa_selecionada)