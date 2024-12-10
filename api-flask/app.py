from flask import Flask, request, jsonify  #essa request esta dentro do flask
from flask_cors import CORS
import json
import os 

app = Flask("Minha Api")
CORS(app)

@app.route("/")
def homepage():
    return "Hello world!"

def cpf_existe(cpf):
    dados_pessoas = carregar_arquivo()
    return cpf in dados_pessoas

@app.route("/consulta", methods=['GET'])
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    return registro

@app.route("/cadastro", methods=["POST"])
def cadastrar():
    payload = request.json
    cpf = payload.get("cpf")

    if cpf_existe(cpf):
        return jsonify(True)

    valores = payload.get("dados")
    salvar_dados(cpf, valores)
    return jsonify(False)


def carregar_arquivo():
    # caminho de onde o arquivo está salvo
    caminho_arquivo = "dados.json"
    try:
        with open(caminho_arquivo, "r") as arq: #chamou de arquivo, criou uma variavel
            return json.load(arq)
    except Exception:
        return "Falha ao carregar o arquivo"

def gravar_arquivo(dados):
    caminho_arquivo = "dados.json"
    try:
        with open(caminho_arquivo, "w") as arq: #chamou de arquivo, criou uma variavel, em escrita W
            json.dump(dados, arq, indent=4) #pegando o dicionario e persistindo isso, no formato json
            return "Dados armazenados"
    except Exception:
        return "Falha ao carregar o arquivo"
    
def salvar_dados(cpf, registro):
    dados_pessoas = carregar_arquivo()
    dados_pessoas[cpf] = registro
    gravar_arquivo(dados_pessoas)

def dados(cpf): #criar unçao carregar arquivo
    dados_pessoas = carregar_arquivo() #não é rota
    vazio={
        "nome": "não encontrado",
        "data_nascimento": "nao encontrado",
        "email": "não encontrado"
    }
    cliente = dados_pessoas.get(cpf, vazio)
    return cliente

if __name__ == "__main__":
    app.run(debug=True)