from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.user_service import UserServices
from src.models import game

class UserDto:
    partida = {
        "minijuego":fields.String(attribute="game.gameName"),
        "score":fields.Integer
    }

    user = {
        "name":fields.String,
        "last_name":fields.String(attribute="last_name"),
        "email":fields.String,
        "birthDate":fields.DateTime,
        "role":fields.String,
        "location":fields.String,
        "partidas": fields.List(fields.Nested(partida)),
        
        "managerPerm":fields.Boolean,
        "aplicantes":fields.List(fields.Nested(super)),
    }
    ##OJO a aplicantes, posible punto de error

    response = {
        "data": fields.Nested(user),
        "message":fields.String
    }

    #STORED PROCEDURES
    ConsMinijuego = {
        "minijuego":fields.String,
        "score":fields.Integer
    }
    ConsPsicometrico = {
        "seccionPsico":fields.String,
        "score":fields.Integer
    }
    ConsPregunta={"details":fields.String}
    
class UserController(Resource):
   
    def post(self):
        data = request.json
        print(data)
        return UserServices.create_user(data["name"],data["email"], data["password"], data["password2"])
    
    @marshal_with(UserDto.response)
    def get(self):
        
        return UserServices.get_user()

class UserControllerFindUser(Resource):
    @marshal_with(UserDto.response)
    def post(self):
        data = request.json
        return UserServices.get_user(data["user_id"])


class UserLoginController(Resource):
    def post(self):
        data = request.json
        print(data)
        return UserServices.login(data["email"], data["password"])

##21 abril
class ConsultaMinijuegoController(Resource):
    @marshal_with(UserDto.partida)
    def get(self, myid):
        return UserServices.execConsultaMinijuego(myid)