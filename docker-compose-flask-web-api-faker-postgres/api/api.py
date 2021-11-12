from flask import Flask, flash,session,jsonify
from db import Session , engine,connection_db
from flask_sqlalchemy import SQLAlchemy
import requests
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
session = Session()
from models import *


@app.route('/crear_registros')
def crear_registros():
    url = 'http://faker-service/datos'
    response = requests.get(url)
    response_json = json.loads(response.text)
    for i in response_json["datos"]:
        data = DataFaker(nombre=i["name"], nombre_compania=i["company_email"], ciudad=i["city"],direccion=i["address"],telefono=i["phone_number"],color=i["color"])
        db.session.add(data)
    db.session.commit()
    return {'data':"Registros creados"}

@app.route('/eliminar_registros')
def eliminar_registros():
    with engine.connect() as con:
        eliminar = "delete from datafaker"
        try:
            respuesta_data = con.execute(eliminar)
            resul = "data eliminada"
        except:
            resul = "Data no eliminada"
        return {'data':resul}

@app.route('/registros_faker')
def registros_faker():
    with engine.connect() as con:
        obtener_data = "select * from datafaker"
        respuesta_data = con.execute(obtener_data)
        lista = list()
        for i in respuesta_data:
            data = dict()
            data["name"] = i[1]
            data["nombre_compania"] = i[2]
            data["ciudad"] = i[3]
            data["direccion"] = i[4]
            data["telefono"] = i[5]
            data["color"] = i[6]
            lista.append(data)
        return {'data':lista}

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
