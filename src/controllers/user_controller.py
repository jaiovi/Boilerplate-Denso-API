from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.user_service import UserServices
from src.models import game

# Se escribe en diccionario para convertirlo fácilmente en un JSON y que pueda ser devuelta correctamente como parte de la respuesta.
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
        "department":fields.String,
        "partidas": fields.List(fields.Nested(partida)),
        
        "managerPerm":fields.Boolean,
        "aplicantes":fields.List(fields.Nested(super)),
        "code":fields.String
    }
    ##OJO a aplicantes, posible punto de error

    response = {
        "data": fields.Nested(user),
        "message":fields.String
    }

    '''#STORED PROCEDURES
    ConsMinijuego = {
        "minijuego":fields.String,
        "score":fields.Integer
    }
    ConsPsicometrico = {
        "seccionPsico":fields.String,
        "score":fields.Integer
    }
    ConsPregunta={"details":fields.String}'''
    

class UserController(Resource):

    # Va a mapear al bojeto que está recibiendo en esto 
    # @marshal_with(UserDTO.user_list, envelope="data") # Lo envuele en una variable que se llama data porque es una lista
    # def get(self): # self es el this de Python
    #     #return "GET UserController" # Regresa un string
    #     return UserServices.get_user()
   

    # return "POST UserController"
        # sacar los datos que estoy recbiiendo
    def post(self):
        data = request.json # request es una variable global
        print(data)
        return UserServices.create_user(data["name"], data["last_name"], data["role"], data["location"], data["birthDate"], data["email"], data["password"], data["validate_password"]) # manda como parámetro name y los demás valores
    
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


class CandidatoController(Resource):
    @marshal_with(UserDto.response)
    def get(self, myid):
        return UserServices.get_user_candidate(myid)

class TablaController(Resource):
    @marshal_with(UserDto.user)
    def get(self, mylocation):
        return UserServices.tabla(mylocation)

class UnityController(Resource):
    @marshal_with(UserDto.user)
    def get(self, mycode):
        return UserServices.unity(mycode)