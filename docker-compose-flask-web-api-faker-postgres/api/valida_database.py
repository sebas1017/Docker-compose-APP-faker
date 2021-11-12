
from db import Session , engine,connection_db

def existe():
    with engine.connect() as con:
        obtener_frutas = "select * from datafaker"
        try:
            respuesta_frutas = con.execute(obtener_frutas)    
            return '1'
        except:
            return '2'

exit(existe()) 
