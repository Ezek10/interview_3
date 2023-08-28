# Entrevista tecnica

## Descripción

Este repositorio esta preparado para la resolucion de la entrevista tecnica propuesta por ___ para un puesto como Python Developer.
Se puede encontrar las condiciones de la entrevista en "Challenge.txt"

## Docker

Descarga la imagen

    docker pull ezemarcel/interview_3_app:latest

Ahora corre la imagen

    docker-compose up

## Instalación

Clone el repositorio: 

    git clone https://github.com/Ezek10/interview_3.git

Cree una unidad virtual: 

    python -m venv .venv

Activar ambiente virtual:

    .\.venv\Scripts\activate

Instale las dependencias:

    pip install -r requirements.txt

## Correr

Para correr el programa corra:

    uvicorn src.main.app:app --reload --env-file .env

o

    make run

## Documentacion Tecnica

Despues de levantar la imagen de Docker puede proceder al siguiente link para revisar la documentacion autogenerada por Swagger:

http://localhost:8080/docs

## Pruebas de uso

Despues de levantar la imagen de Docker, puede probar los siguientes comandos de 2 formas:

Desde la pagina de documentacion en:

http://localhost:8080/docs

O manualmente desde la terminal:

    curl --location 'http://localhost:8080/status'

### POST

Crear carreras nuevas:

    curl --location 'http://localhost:8080/carrers' \
    --header 'admin-auth: admin' \
    --header 'Content-Type: application/json' \
    --data '[
        {
            "id": 1,
            "name": "Ingenieria en Comunicaciones"
        },
        {
            "id": 2,
            "name": "Ingenieria en Sistemas"
        },
        {
            "id": 3,
            "name": "Ingenieria en Electronica"
        },
        {
            "id": 4,
            "name": "Ingenieria Mecanica"
        }
    ]'

Crear Materias nuevas:

    curl --location 'http://localhost:8080/subjects' \
    --header 'admin-auth: admin' \
    --header 'Content-Type: application/json' \
    --data '{
        "subjects": [
            {
                "id": 1,
                "name": "Electronica Aplicada 1"
            },
            {
                "id": 2,
                "name": "Mecanica Aplicada 1"
            },
            {
                "id": 3,
                "name": "Quimica"
            },
            {
                "id": 4,
                "name": "Algebra"
            }
        ]
    }'

Crear las curriculas de las carreras:

    curl --location 'http://localhost:8080/curriculas' \
    --header 'admin-auth: admin' \
    --header 'Content-Type: application/json' \
    --data '{
        "curriculas": [
            {
                "carrer_id": 1,
                "subjects_ids": [1,3,4]
            },
            {
                "carrer_id": 2,
                "subjects_ids": [4]
            },
            {
                "carrer_id": 3,
                "subjects_ids": [1,3,4]
            },
            {
                "carrer_id": 4,
                "subjects_ids": [2,3,4]
            }
        ]
    }'

Crear el primer Lead:

    curl --location 'http://localhost:8080/leads' \
    --header 'Content-Type: application/json' \
    --data-raw '[
        {
            "person": {
                "name": "Jhon Doe",
                "email": "JhonDoe@gmail.com",
                "address": "somewere",
                "phone": "543512513515"
            },
            "subjects": [
                {
                    "id": 3,
                    "attempt": 1
                },
                {
                    "id": 1,
                    "attempt": 2
                }
            ],
            "carrers":[
                {
                    "id": 1,
                    "registration_year": 2021
                },
                {
                    "id": 2,
                    "registration_year": 2020
                }
            ]
        }
    ]'

### GET

Carreras:

    curl --location 'http://localhost:8080/carrers' \
    --header 'admin-auth: admin' \
    --data ''

Curriculas:

    curl --location 'http://localhost:8080/curriculas?admin-auth=admin' \
    --header 'admin-auth: admin' \
    --data ''

Materias:

    curl --location 'http://localhost:8080/subjects?admin-auth=admin' \
    --header 'admin-auth: admin' \
    --data ''

Leads:

    curl --location 'http://localhost:8080/leads?page=1' \
    --header 'admin-auth: admin' \
    --data ''

Lead:

    curl --location 'http://localhost:8080/leads/lead/1' \
    --data ''



### DELETE

Carrera:

    curl --location --request DELETE 'http://localhost:8080/carrers/1' \
    --header 'admin-auth: admin' \
    --data ''

Curricula:

    curl --location --request DELETE 'http://localhost:8080/curriculas/1?admin-auth=admin' \
    --header 'admin-auth: admin' \
    --data ''

Materia:

    curl --location --request DELETE 'http://localhost:8080/subjects/1?admin-auth=admin' \
    --header 'admin-auth: admin' \
    --data ''

Lead:

    curl --location --request DELETE 'http://localhost:8080/leads/lead/1' \
    --data ''


## Debbug in VSCode

Copiar el siguiente codigo en .vscode/launch.json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Uvicorn run",
                "type": "python",
                "cwd": "${workspaceFolder}/",
                "request": "launch",
                "program": "${workspaceFolder}/.venv/Scripts/uvicorn.exe",
                "args": [
                    "src.main.app:app"
                ],
                "console": "integratedTerminal",
                "justMyCode": true,
                "envFile": "${workspaceFolder}/.env"
            }
        ]
    }

## Tests

Para correr los tests de esta aplicacion se recomienda usar el siguiente comando 

    pytest --cov --cov-config=.coveragerc --cov-report=html

o

    make test

puede abrir el archivo **htmlcov/index.html** para ver el coverage generado de los tests

## Cómo contribuir

Si bien este proyecto solo implica los conocimientos al momento de hacer esta entrevista creo que siempre puede ser bueno saber como se puede mejorar una entrega de este tipo, desde la funcionalidad del codigo, los tests hasta la documentacion o la presentacion del corriente archivo.

Si alguien se siente en capacidad de aportar sientase libre de crear una rama nueva y con un PR aportar sus ideas para mejorar esta presentacion

## Notas

- Si bien hay algunas cosas que se podrian implementar no se hizo debido al alcance del ejercicio como Github Actions para realizar un Coverage Badge
