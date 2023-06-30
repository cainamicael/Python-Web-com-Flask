from flask import Flask, request, render_template, redirect, url_for
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', user='root', password='', database='youtube')

@app.route('/clientes', methods=['GET'])
def main():
    cursor = db.cursor()
    sql = 'SELECT * FROM clientes'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    
    return render_template('index.html', content=results)

@app.route('/clientes', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    
    cursor = db.cursor()
    sql = 'INSERT INTO clientes (nome, email) VALUES (%(nome)s, %(email)s)'
    res = cursor.execute(sql, {'nome': nome, 'email': email})
    db.commit()
    
    return redirect(url_for('main')) #O nome da função do endpoint que queremos

@app.route('/deletar') #/deletar?id={{elemento[0]}}
def delete():
    id = request.args.get('id')
    return f'O id é {id}'

app.run(port=5000, host='localhost', debug=True)
