from sqlalchemy import Column,String , Integer
#from db import Base,engine
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship
from api import db

class DataFaker(db.Model):
    __tablename__ = 'datafaker'
    id = db.Column(db.Integer,autoincrement=True , primary_key=True)
    nombre = db.Column(db.String(255))
    nombre_compania = db.Column(db.String(100))
    ciudad = db.Column(db.String(120))
    direccion = db.Column(db.String(200))
    telefono = db.Column(db.String(40))
    color = db.Column(db.String(40))
