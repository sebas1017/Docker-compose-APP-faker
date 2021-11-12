#!/bin/bash
va=$(python valida_database.py 2>&1)
if [[ $va -ne '1' ]];
then
    python manage.py db init
fi

if [ -d /usr/src/app/migrations ]   # For file "if [ -f /home/rama/file ]"
then
    echo "Existe migraciones significa que no se volvio a construir la imagen"
else
    # Elimina la tabla de migraciones de la bd
    python elimina_tabla_alembic.py
    python manage.py db init
fi
python manage.py db migrate
python manage.py db upgrade
echo $va
python api.py 

