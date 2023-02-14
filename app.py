from flask import Flask, jsonify , request, Response
from http import HTTPStatus
import json
import urllib

app = Flask(__name__)
if __name__ == "__main__":
 app.run(debug = True)

with open('\"Archivos_JSON/usuarios.json', encoding='utf-8') as archivo_json:
    usuarios = json.load(archivo_json)
@app.route('/')
def home():
 return 'SISTEMA DE ENTRADAS: CINE'

@app.route('/')
def devolver_usuarios():
    return jsonify(usuarios)
    