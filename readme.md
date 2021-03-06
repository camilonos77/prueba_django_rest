## Prueba técnica Abraxas

## Presentado por Camilo A. Pulido
## contacto: camilo.pr.77190@gmail.com

## Pasos para desplegar el proyecto

## 1. Configuración de Docker


En la primera parte se realizará la construcción de la imagen para el contenedor de la base de datos PostgreSQL. Por favor ejecute el siguiente comando

 - sudo docker build -t image_db -f Dockerfile_db . 

Ya que se tiene la imagen del contenedor de la base de datos, se deberá iniciar el contenedor a través del siguiente comando

-   sudo docker run --name db_django  --net=host  -e POSTGRES_PASSWORD=mysecretpassword -d image_db

Ahora si se inicio correctamente el contenedor de la base de datos
podemos crear la base de datos para que Django pueda iniciar
el servicio web correctamente. (Por favor esperar al menos 30 segundos para lanzar los siguientes comandos mientras inician todos los servicios de POSTGRES)

-   sudo docker exec -it db_django psql -U postgres  -c "CREATE DATABASE test_django ENCODING 'UTF8';"

- sudo docker exec -it db_django psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE test_django TO postgres;"





El segundo paso es realizar la construcción de la imagen del contenedor para ejecutar el proyecto de Django

Lanzar el comando
-   sudo docker build . -t django_prueba_2

Posteriormente se debe iniciar el contenedor con el siguiente comando 

 -  sudo docker-compose up


Finalmente se puede acceder al Api desde la url: localhost:8000


Los servicios que se pueden consumir son los siguientes:

    - http://localhost:8000/api/v1/rows
    -   http://localhost:8000/api/v1/datasets




## Otros comandos

Si se desean correar las pruebas unitarias ejecute el siguiente comando ingresando al contenedor de Django via bash:

    python manage.py test .



Si se desea iniciar los contenedores luego de haber ejecutado los pasos anteriores y los contenedores estan apagados, se debe correr los siguientes comandos:

    Para iniciar la base de datos

    sudo docker ps -a 

    Con este comando saldra la lista de contenedores, luego se debe buscar el ID del contenedor con nombre image_db

    y asi se debe generar el siguiente comando

    sudo docker start ID_CONTAINER

    Para iniciar Django

    sudo docker-compose up