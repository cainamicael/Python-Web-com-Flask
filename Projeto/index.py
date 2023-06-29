from flask import Flask, render_template

app = Flask(__name__)

#Rotas
@app.route('/')
def hello_world():
    return render_template('index.html', content=['banana', 'pera', 'maçã'])

@app.route('/sobre')
def sobre():
    return '<h2>Sobre</h2>'

#pegando parâmetro da url
@app.route('/noticia/<slug>')
def noticia(slug):
    return f'<h2>O slug é {slug}</h2>'
