from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.user_service import UserServices

class UserDto:
    candidato = {
        "name":fields.String,
        "email":fields.String,
    }

    user = {
        "name":fields.String,
        "email":fields.String,
        "candidatos": fields.List(fields.Nested(candidato)),
    }

    response = {
        "data": fields.Nested(user),
        "message":fields.String
    }
    
class UserController(Resource):
   
    def post(self):
        data = request.json
        print(data)
        return UserServices.create_user(data["name"],data["email"], data["password"], data["validate_password"])
    
    @marshal_with(UserDto.response)
    def get(self):
        
        return UserServices.get_user()

class UserControllerFindUser(Resource):
    @marshal_with(UserDto.response)
    def post(self):
        data = request.json
        return UserServices.get_user(data["id"])


class UserLoginController(Resource):
    def post(self):
        data = request.json
        print(data)
        return UserServices.login(data["email"], data["password"])
