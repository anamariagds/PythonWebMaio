from flask import Flask, render_template, g, flash, url_for, request, redirect, abort, session
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

#Rota de login do usuário
@app.route("/login", methods=["POST", "GET"])
def login():
    erro = None
    if(request.method == "POST"):
        if request.form['username'] == "Ocean" and request.form['password']=="1234":
            session['logado'] = True
            flash("Usuario logado" + request.form['username'])
            return redirect(url_for('exibir_posts'))
        erro = "Usuário ou senha incorretos" 
    return render_template("login.html", erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado', None)

    flash("Logout Efetuado")
    return redirect(url_for('exibir_posts'))

@app.route('/inserir', methods=['POST', 'GET'])
def inserir():
    if not session.get('logado'):
        abort(401)
    titulo = request.form.get('titulo')
    texto = request.form.get('texto')
    sql = "INSERT INTO posts(titulo, texto) VALUES(?, ?)"
    g.bd.execute(sql,[titulo,texto])
    g.bd.commit()
    flash('Novo post  inserido')
    return redirect(url_for('exibir_posts'))

#Função para a criação da rota de exibição de post e busca dos posts na tela
@app.route('/')
def exibir_posts():
    sql = "SELECT titulo, texto, data_criacao FROM  posts ORDER BY id DESC"
    resultado = g.bd.execute(sql) #executa a busca que está na variavel sql
    posts = []

    for titulo, texto, data_criacao in resultado.fetchall():
        posts.append({
            "titulo": titulo,
            "texto": texto,
            "data_criacao": data_criacao
        })
    return render_template('exibir_posts.html', posts=posts)

@app.route('/aluno')
def aluno():
    return "Diego, Geissy, Guilherme, Sthefany"