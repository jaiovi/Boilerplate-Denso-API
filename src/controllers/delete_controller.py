from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.game_service import GameServices
from src.models import game

class DeleteDto:
    response = {
        "message":fields.String
    }

class DeleteUserController(Resource):
    @marshal_with(DeleteDto.response)
    def get(self, myid):
        return GameServices.execDeleteUser(myid)

class DeleteTestsController(Resource):
    @marshal_with(DeleteDto.response)
    def get(self, myid):
        return GameServices.execDeleteTests(myid)