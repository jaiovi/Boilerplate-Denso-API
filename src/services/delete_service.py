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
from sqlalchemy import delete

class DeleteServices:
    @staticmethod
    def deleteUser(myid):
        comprobar = User.query.filter_by(user_id=myid, managerPerm=0).first()
        if comprobar:
            ejecutar = db.session.execute(sqlalchemy.text("CALL SP_DeleteUser(:param)"), {"param":myid}).fetchall()
            print(myid)
            db.session.commit()
            return {"message":"Usuario completo eliminado"}
        else:
            return {"message":"Usuario inexistente para eliminar"}

    @staticmethod
    def deleteTests(myid):
        #psicometrico = Partida.query.filter(user_id==myid).delete() https://stackoverflow.com/questions/27158573/how-to-delete-a-record-by-id-in-flask-sqlalchemy
        comprobar = Partida.query.filter_by(player_id=myid).first()
        if comprobar:
            ejecutar = db.session.execute(sqlalchemy.text("CALL SP_DeleteTests(:param)"), {"param":myid}).fetchall()
            print(myid)
            db.session.commit()
            return {"message":"Examenes y minijuegos limpiados"}
        else:
            return {"message":"Usuario sin examenes ni minijuegos"}