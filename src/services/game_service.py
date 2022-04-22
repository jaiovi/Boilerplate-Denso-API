from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from src.models.test import Test #ahi el error, aqui correcion 6a
from database import db

import sqlalchemy

class GameServices:
    ###SERVICIOS NUEVOS
    @staticmethod
    def execConsultaMinijuego(myid):
        #directamente con tus modelos.
        minijuegos = Partida.query.filter_by(player_id=myid).all()
        print(minijuegos)
        return minijuegos
    
    @staticmethod
    def execConsultaPsicometrico(myid):
        psicometrico = db.session.execute(sqlalchemy.text("CALL SP_ConsultaPsicometrico(:param)"), {"param":myid}).fetchall()
        ##psicometrico = Game.query.join(Question).filter(Answer.user_id==myid).all()
        print(psicometrico)
        return psicometrico