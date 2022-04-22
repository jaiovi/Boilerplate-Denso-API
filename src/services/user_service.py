from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from src.models.test import Test #ahi el error, aqui correcion 6a
from database import db

import sqlalchemy

class UserServices:
    '''
    @marshal_with(UserDto.response)
    def post(self):
        data=request.json
        print(data)
        print((not "namex" in data))
        if not "namex" in data:
    '''        

    @staticmethod
    def get_user():
        user = User.current_user()
        

        if not user:
            return {"message":"Usuario inexistente", "data":user}

        return {"message":"Usuario encontrado", "data":user}


    @staticmethod
    def create_user(name, email, password, validate_password, last_name, role, location, managerPerm): #nos falta age

        if email != "^\w+(@na.denso.com)$":
            return {"message":"Su dirección de correo no tiene los permisos para acceder.", "success":False}, 400

        if password != validate_password:
            return {"message":"Las contraseñas son diferentes.", "success":False}, 400
         
        #new_user = User(name=name, email=email, password=password)
        new_user = User(name=name, email=email, password=password, last_name=last_name, role=role, location=location, managerPerm=managerPerm, manager_id=manager_id) #nos falta age

        db.session.add(new_user)
        db.session.commit()

        return {"message":"Usuario creado correctamente", "success":True}

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"message":"Usuario no encontrado", "success":False}, 404
        
        if not user.check_password(password):
            return {"message":"Contraseña incorrecta", "success":False}, 404

        session = Session.open()
        session.set("user_id",user.user_id )
        session.save()

        print(session.get("token"))
        
        return {"message":"Login exitoso","token":session.get("token"), "success":True} 

    

'''
def execConsultaPerfil(myid)
    consulta = db.session.execute(sqlalchemy.text("CALL SP_ConsultaMinijuego(:param)"), param=myid)
    return consulta

def getPregunta(mypreguntaid) #para el videojuego
    ConsPregunta = Question.query.filter_by(mypreguntaid=session.get("question_id")).first()
    return ConsPregunta
def postRespuesta(myid, mypreguntaid, myrespuesta)
    new_answer = Answer(question_id=mypreguntaid, user_id=myid, scale_num=myrespuesta)
    db.session.add(new_answer)
    db.session.commit
    return {"message":"Respuesta anadida", "success":True}'''