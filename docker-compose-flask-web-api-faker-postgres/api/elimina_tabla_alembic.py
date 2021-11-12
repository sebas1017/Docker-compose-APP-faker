
from db import Session , engine,connection_db

with engine.connect() as con:
    elimina_tabla = "drop table alembic_version"
    try:
        elimina = con.execute(elimina_tabla)    
    except:
        pass
