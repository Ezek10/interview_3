# FinanzasWP

## Table of Contents

* [Descripción](#descripción)
* [Requisitos](#requisitos)
* [Docker](#docker)
* [Instalación](#instalación)
* [Uso](#uso)
* [Debbug in VSCode](#debbug-in-vscode)
* [Tests](#tests)
* [Cómo contribuir](#cómo-contribuir)

## Descripción

Este proyecto esta destinado a realizar un repositorio de ejemplo con la utilizacion de FastAPI y el uso de una arquitectura hexagonal
o arquitectura domain-adapter.
Como caso de uso se realizo una aplicacion de finanzas personales con la particularidad que recibe y envia informacion por Whatsapp.
Para ello se creo una cuenta de Meta con el objetivo de interactuar con la API de Whatsapp.
Esta aplicacion requiere de una cuenta verificada de Meta Buisness con datos legales de la empresa para ponerla en funcionamiento pleno, por ello es que no se encuentra en produccion. (Cualquier ayuda es bienvenida)

## Requirements

* Python 3.10
* Docker
* Docker Compose

## Docker

Descarga la imagen

    docker pull ezemarcel/finanzaswp:latest

Ahora corre la imagen

    docker run --name finanzaswp --rm -p 8000:80 ezemarcel/finanzaswp

## Instalación

Clone el repositorio: 

    git clone https://github.com/Ezek10/Finanzaswp.git

Cree una unidad virtual: 

    python -m venv .venv

Activar ambiente virtual:

    .\.venv\Scripts\activate

Instale las dependencias:

    pip install -r requirements.txt

## Uso

Para correr el programa corra:

    uvicorn src.main.app:app --env-file .env-dev

o

    make run

y luego realice la siguiente request para verificar si esta corriendo:

    curl --location 'http://localhost:8000/status'

y luego puede probar con el siguiente para verificar su funcionamiento (reemplazar el PHONE_NUMBER y TIMESTAMP)

    curl --location 'http://localhost:8000/whats_app' \
    --header 'Content-Type: application/json' \
    --data '{
        "object": "whatsapp_business_account",
        "entry": [{
            "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
            "changes": [{
                "value": {
                    "messaging_product": "whatsapp",
                    "metadata": {
                        "display_phone_number": "PHONE_NUMBER",
                        "phone_number_id": "PHONE_NUMBER_ID"
                    },
                    "contacts": [{
                        "profile": {
                        "name": "NAME"
                        },
                        "wa_id": "PHONE_NUMBER"
                    }],
                    "messages": [{
                        "from": "PHONE_NUMBER",
                        "id": "wamid.ID",
                        "timestamp": "TIMESTAMP",
                        "text": {
                        "body": "listar categorias"
                        },
                        "type": "text"
                    }]
                },
                "field": "messages"
            }]
        }]
    }'

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
                "envFile": "${workspaceFolder}/.env-dev"
            }
        ]
    }

## Tests (TODO)

Para correr los tests de esta aplicacion se recomienda usar el siguiente comando 

    pytest --cov --cov-config=.coveragerc --cov-report=html

o

    make test

puede abrir el archivo **htmlcov/index.html** para ver el coverage generado de los tests

## Cómo contribuir

Cualquier idea que sea para mejorar el proyecto o simplemente implementar algo que aporte a todos los que lo lean es bienvenido, siempre la idea
es tener un proyecto que sirva como template donde uno pueda usar las cosas implementadas aqui, desde arquitecturas nuevas hasta uso de nuevas tecnologias.

Si alguien se siente en capacidad de aportar sientase libre de crear una rama nueva y con un PR aportar sus ideas para mejorar esta presentacion
