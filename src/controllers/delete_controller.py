from email import message
from flask import request
from flask_restful import fields, marshal_with
from flask_restful import Resource
from src.services.game_service import GameServices
from src.models import game

class DeleteUserController(Resource):
    def get(self, myid):
        return GameServices.execDeleteUser(myid)

class DeleteTestsController(Resource):
    def get(self, myid):
        return GameServices.execDeleteTests(myid)