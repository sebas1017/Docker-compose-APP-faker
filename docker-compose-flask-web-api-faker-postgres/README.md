# Iniciar el proyecto
    - docker-compose build
    - docker-compose up

Luego de que los contenedores esten arriba , se puede validar si todos se subieron de la manera correcta usando:
    - docker ps

Puertos habilitados para los contenedores:

    - 5000 -> El objetivo del contenedor que esta en este puerto es por medio de los botones consumir las apis que se crearon en el contenedor de api-service.

    - 5001 -> El unico objetivo del contenedor que se encuentra en este puerto es responder las solicitudes que le envia la app de la web.
    
    - 5002 -> El unico objetivo del contenedor que se encuentra en este puerto es generar 13 datos aleatorios los cuales son (nombre,nombre_compania,ciudad,direccion,telefono) , se puede validar si el contenedor esta funcionando es realizando el proceso por postman (El unico metodo que recibe esta api es de tipo GET ) http://localhost:5002/datos

