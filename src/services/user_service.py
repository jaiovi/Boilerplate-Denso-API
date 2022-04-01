from src.models.user import User
from src.models.candidato import Candidato
from src.models.session import Session
from database import db

class UserServices:
    @staticmethod
    def get_user():
        user = User.current_user()
        

        if not user:
            return {"message":"Usuario inexistente", "data":user}

        return {"message":"Usuario encontrado", "data":user}


    @staticmethod
    def create_user(name, email, password, validate_password):

        if password != validate_password:
            return {"message":"Las contraseñas son diferentes", "success":False}, 400
         
        new_user = User(name=name, email=email, password=password)

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