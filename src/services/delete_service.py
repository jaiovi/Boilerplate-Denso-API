from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from src.models.test import Test
from database import db

import sqlalchemy
from datetime import date

class DeleteServices:
    @staticmethod
    def deleteUser(myid):
        #db.session.delete(arreglo_almacenado) - query normal
        psicometrico = db.session.execute(sqlalchemy.text("CALL SP_DeleteUser(:param)"), {"param":myid}).fetchall()
        if not psicometrico:
            return {"message":"Usuario inexistente"}
        return {"message":"Usuaario completo eliminado"}

    @staticmethod
    def deleteTests(myid):
        psicometrico = db.session.execute(sqlalchemy.text("CALL SP_DeleteTests(:param)"), {"param":myid}).fetchall()
        if not psicometrico:
            return {"message":"Usuario inexistente"}
        return {"message":"Usuario con examen limpio"}