from flask import Flask, render_template

app = Flask("Olá") #referencia a aplicação

@app.route('/')
def ola():
    return render_template('ola.html')