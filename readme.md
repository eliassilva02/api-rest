# API REST com Flask

Este é uma aplicação Flask que cria uma API REST usando Pydantic e TinyDB.

## Requisitos
- Python 3.11
- Flask
- Flask-Pydantic-Spec
- Pydantic
- TinyDB

## Endpoints
| Endpoint         | Métodos | Regra                                |
|----------------- | ------- | ------------------------------------ |
| Atualiza uma pessoa  | PUT     | /pessoas/{id}                    |
| Deleta uma pessoa    | DELETE  | /pessoas/{id}                    |
| Insere um pessoa    | POST    | /pessoas                             |
| Busca uma pessoa     | GET     | /pessoas/{id}                    |
| Busca todas as pessoas    | GET     | /pessoas                             |
| Redoc   | GET     | /apidoc/redoc                        |
| Swagger | GET     | /apidoc/swagger                      |
| OpenApi          | GET     | /apidoc/openapi.json                 |


