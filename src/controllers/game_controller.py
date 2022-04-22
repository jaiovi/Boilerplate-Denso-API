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

##21 abril
class ConsultaMinijuegoController(Resource):
    @marshal_with(GameDto.partida)
    def get(self, myid):
        return GameServices.execConsultaMinijuego(myid)

class ConsultaPsicometricoController(Resource):
    @marshal_with(GameDto.partida2) # le da el formato a json
    def get(self, myid):
        return GameServices.execConsultaPsicometrico(myid)