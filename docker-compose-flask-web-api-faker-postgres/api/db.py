import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection_db = f'postgresql://{user}:{password}@{host}:{port}/{database}'

#connection_db = f'postgresql://postgres:postgres@db:5432/postgres'
connection_db = 'postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev'

Base = declarative_base()

engine = create_engine(connection_db)

Session = sessionmaker(bind=engine)
