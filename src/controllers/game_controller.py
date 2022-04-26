from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.game_service import GameServices
from src.models import game

class GameDto:
    partida = {
        "minijuego":fields.String(attribute="game.gameName"),
        "score":fields.Integer
    }
    partida2 = {
        "seccionPsico":fields.String,
        "puntos":fields.Integer
    }
    pregunta = {
        "question_id":fields.Integer,
        "details":fields.String
    }
    respuesta = {
        "question_id":fields.String(attribute="question.details"),
        "scale_num":fields.Integer,
        "user_id":fields.Integer
    }

##21 abril
class ConsultaMinijuegoController(Resource):
    @marshal_with(GameDto.partida)
    def get(self, myid):
        return GameServices.execConsultaMinijuego(myid)

class ConsultaPsicometricoController(Resource):
    @marshal_with(GameDto.partida2) # le da el formato a json
    def get(self, myid):
        return GameServices.execConsultaPsicometrico(myid)

#UNITY
class PreguntaController(Resource):
    @marshal_with(GameDto.pregunta)
    def get(self, mypreguntaid):
        return GameServices.execPregunta(mypreguntaid)

class RespuestaController(Resource):
    def post(self):
        data = request.json
        print(data)
        return GameServices.createRespuesta(data["scale_num"],data["question_id"], data["user_id"])