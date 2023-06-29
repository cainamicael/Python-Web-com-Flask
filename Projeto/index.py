from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
app.secret_key = 'vad6gq883JYTI!&uhje31ljhj,cw$%¨defkqrq8'

#Rotas
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        nome = request.form['nome']
        idade = request.form['idade']
        conteudo = request.form['conteudo']
        
        col = {'nome': nome, 'idade': idade, 'conteudo': conteudo} #collection
        
        return f"O que veio do meu form: {col}" #o name do formulario

@app.route('/sobre')
def sobre():
    return '<h2>Sobre</h2>'

#pegando parâmetro da url
@app.route('/noticia/<slug>')
def noticia(slug):
    return f'<h2>O slug é {slug}</h2>'

@app.route('/sessao')
def sessao():
    if 'usuario' in session:
        usuario = session['usuario']
        return usuario
    else:
        session['usuario'] = 'guilherme' 
        return session['usuario'] 
    
@app.route('/cookie')
def cookie():
    #Pegando cookie
    if (request.cookies.get('usuario')):
        resp = make_response('Meu website com o cookie setado')
    else:
        #Setando cookie
        resp = make_response('Meu website sem o cookie')
        resp.set_cookie('usuario', 'guilherme')    
    
    return resp
    

