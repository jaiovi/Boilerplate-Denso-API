from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from src.models.test import Test #ahi el error, aqui correcion 6a
from database import db

import re
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
    def create_user(name, last_name, role, location, birthDate, email, password, validate_password): #nos falta age data["managerPerm"]
        managerPerm=0
        if re.search("^\w+(@na\.denso\.com)$", email):
            managerPerm=1
            #return {"message":"Su dirección de correo no tiene los permisos para acceder.", "success":False}, 400
        print(managerPerm)

        if password != validate_password:
            return {"message":"Las contraseñas son diferentes.", "success":False}, 400

        new_user = User(name=name, email=email, password=password, last_name=last_name, role=role, location=location, managerPerm=managerPerm, birthDate=birthDate) #nos falta age manager_id=manager_id,

        db.session.add(new_user)
        db.session.commit()

        mensajito = string("Usuario creado correctamente con managerPerm "+ managerPerm)
        return {"message":mensajito, "success":True}

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

    @staticmethod
    def get_user_candidate(user_id):
        candidato = User.query.filter_by(user_id=user_id, managerPerm=0).first()
        #candidato = db.session.execute(sqlalchemy.text("CALL SP_ConsultaPerfil(:param)"), {"param":user_id}).fetchall()
        print(candidato)
        return {"message":"Candidato existente", "data":candidato}

    @staticmethod
    def tabla(mylocation):
        print(mylocation)
        candidato = User.query.filter_by(location=mylocation, managerPerm=0).all()
        return candidato#{"message":"Candidatos de locacion dados", "data":candidato}