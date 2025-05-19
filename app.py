from flask import Flask, render_template, abort, redirect, request
import json

app = Flask(__name__)

def owasp10():
    with open("data/owasp.json", encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/xxxs', methods=['GET'])
def xxxs():
    return render_template('xxxs.html')

@app.route('/listaxxxs', methods=['POST'])
def listaxxxs():
    termino = request.form.get('nombre_xxx', '').lower()
    datos = owasp10()
    if termino:
        resultados = [v for v in datos if termino in v['nombre'].lower()]
    else:
        resultados = datos
    return render_template('listaxxxs.html', resultados=resultados)

@app.route('/xxx?id=<identificador>')
def detalle(identificador):
    datos = owasp10()
    item = next((v for v in datos if v['id'] == identificador), None)
    if not item:
        return abort(404)
    return render_template('detalle_xxx.html', item=item)

@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0",5000,debug=True)
