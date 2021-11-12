from flask import Flask, render_template, request, redirect, url_for,jsonify
import requests
import json
app = Flask(__name__)


def datos():
    url = 'http://api-service:5001/registros_faker'
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json

@app.route('/', methods=['GET', 'POST'])
def index():
    # Renderizar la cantidad de registros
    datos_actuales = datos()
    return render_template('index.html',data=datos_actuales["data"])

@app.route('/registros', methods=['GET'])
def registros(): 
    # Renderizar la cantidad de registros
    url = 'http://api-service:5001/registros_faker'
    response = requests.get(url)
    response_json = json.loads(response.text)

    return jsonify({"data":response_json["data"]})

@app.route('/eliminar_registros', methods=['POST'])
def eliminar_registros(): 
    # Renderizar la cantidad de registros
    url = 'http://api-service:5001/eliminar_registros'
    response = requests.get(url)
    return jsonify({"data":[]})

@app.route('/crear_registros', methods=['POST'])
def crear_registros():
    #Crear registros
    url = 'http://api-service:5001/crear_registros'
    response = requests.get(url)
    # Carga tabla con los datos actuales
    datos_actuales = datos()
    return jsonify({"data":datos_actuales["data"]})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
