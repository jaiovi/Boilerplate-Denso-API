from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from src.models.test import Test #ahi el error, aqui correcion 6a
from database import db

import sqlalchemy
from datetime import datetime

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

    #UNITY
    @staticmethod
    def execPregunta(mypreguntaid):
        pregunta = Question.query.filter_by(question_id=mypreguntaid).first()
        return pregunta
    
    @staticmethod
    def createRespuesta(scale_num,question_id,user_id):
        new_answer = Answer(scale_num=scale_num,question_id=question_id,user_id=user_id)
        db.session.add(new_answer)
        db.session.commit()
        print("Respuesta anadida correctamente")
        return 0

    @staticmethod
    def createPartida(score, game_id, player_id): #identico a user_id
        now = datetime.now()
        new_partida = Partida(score=score,game_id=game_id,player_id=player_id, timeStamp=now)
        db.session.add(new_partida)
        db.session.commit()
        print("Partida anadida correctamente")
        return 0
