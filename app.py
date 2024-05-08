from flask import Flask

app = Flask("Olá") #referencia a aplicação

@app.route('/')
def ola():
    return "Olá mundo!"