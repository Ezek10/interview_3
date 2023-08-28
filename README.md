# Entrevista tecnica

## Descripción

Este repositorio esta preparado para la resolucion de la entrevista tecnica propuesta por ___ para un puesto como Python Developer.
Se puede encontrar las condiciones de la entrevista en "Challenge.txt"

## Docker

Descarga la imagen

    docker pull ezemarcel/interview_3_app:latest

Ahora corre la imagen

    docker run --name talana --rm -p 8000:80 ezemarcel/interview_3_app

## Instalación

Clone el repositorio: 

    git clone https://github.com/Ezek10/interview_3.git

Cree una unidad virtual: 

    python -m venv .venv

Activar ambiente virtual:

    .\.venv\Scripts\activate

Instale las dependencias:

    pip install -r requirements.txt

## Uso

Para correr el programa corra:

    uvicorn src.main.app:app --reload --env-file .env

o

    make run

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
