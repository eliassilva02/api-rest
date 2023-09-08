from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query
from typing import Optional
from itertools import count

app = Flask(__name__)

spec = FlaskPydanticSpec('flask', title='API-REST')
spec.register(app)

database = TinyDB('database.json')
nextID = count()


class Pessoa(BaseModel):
    # ADICIONA O PROXIMO ID COMO O PADRAO
    id: Optional[int]
    nome: str
    idade: int


class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count: int


@app.get('/pessoas')
@spec.validate(resp=Response(HTTP_200=Pessoas))
def SearchPersons():
    """Retorna todas as Pessoas da base de dados."""

    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count=len(database.all())
        ).dict()
    )


@app.get('/pessoas/<int:id>')
@spec.validate(resp=Response(HTTP_200=Pessoa))
def SearchPerson(id):
    """Retorna as pessoas da base de dados."""
    try:
        pessoa = database.search(Query().id == id)[0]
    except IndexError:
        return {'message': 'Pessoa não encontrada!'}, 404

    return jsonify(pessoa)


@app.post('/pessoas')
# DEFINE O CORPO E A RESPOSTA DA API NO SWAGGER
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def InsertPersons():
    # COLOCA A STRING NO SWAGGER
    """Insere pessoas na base de dados."""

    data = request.json

    database.insert(data)

    return data


@app.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def AlterPersons(id):
    """Altera as pessoas da base de dados."""
    query = Query()

    json = request.json

    database.update(json, query.id == id)

    return jsonify(json), 201


@app.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def DeletePersons(id):
    """Deleta pessoas da base de dados."""
    query = Query()
    database.remove(query.id == id)

    return jsonify({'message': 'Pessoa deletada com sucesso.'}), 204


if __name__ == '__main__':
    app.run(debug=True)
