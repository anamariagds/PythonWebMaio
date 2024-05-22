from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "1234"
app = Flask("Olá") #referencia a aplicação

#carrega as configurações especificas da aplicação
app.config.from_object(__name__) 

#coneta com o banco de dados
def conectar():
    return sqlite3.connect(DATABASE)

#conecta antes da resquisição
@app.before_request
def before_request():
    g.bd = conectar()

#Encerra conexão com o banco de dados
@app.teardown_request
def teardown_request(f): #o f não é nada, é por padrão.
    g.bd.close()

#Função para a criação da rota de exibição de post e busca dos posts na tela
@app.route('/')
def exibir_posts():
   # sql = "SELECT titulo, texto, data_criacao FROM  posts ORDER BY id DESC"
   # resultado = g.bd.execute(sql) #executa a busca que está na variavel sql

    posts = [{"titulo": "Titulo 1", "texto":"texto 1", "data_criacao":"21/05/2024"},
            {"titulo": "Titulo 2", "texto":"texto 2", "data_criacao":"22/05/2024"},
            {"titulo": "Titulo 3", "texto":"texto 3", "data_criacao":"23/05/2024"},
            ]

    return render_template('ola.html', posts=posts)

@app.route('/aluno')
def aluno():
    return "Diego, Geissy, Guilherme, Sthefany"