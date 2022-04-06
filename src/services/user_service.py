from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from database import db
import re

class UserServices:
    @staticmethod
    def get_user():
        user = User.current_user()
        

        if not user:
            return {"message":"Usuario inexistente", "data":user}

        return {"message":"Usuario encontrado", "data":user}


    @staticmethod
    def create_user(name, email, password, validate_password, last_name, role, location, managerPerm): #nos falta age

        if email != "^\w+(@denso.com)$":
            return {"message":"Su dirección de correo no tiene los permisos para acceder.", "success":False}, 400

        if password != validate_password:
            return {"message":"Las contraseñas son diferentes.", "success":False}, 400
         
        #new_user = User(name=name, email=email, password=password)
        new_user = User(name=name, email=email, password=password, last_name=last_name, role=role, location=location, managerPerm=managerPerm) #nos falta age

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
        session.set("user_id",user.id )
        session.save()

        print(session.get("token"))
        
        return {"message":"Login exitoso","token":session.get("token"), "success":True} 