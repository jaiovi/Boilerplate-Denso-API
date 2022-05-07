from src.models.user import User
from src.models.partida import Partida
from src.models.session import Session

from src.models.question import Question
from src.models.game import Game
from src.models.answer import Answer
from src.models.test import Test #ahi el error, aqui correcion 6a
from database import db

import re # Para validar el correo
# Para generar el código de acceso
import string
import random

import sqlalchemy # Para la DB y SQL

class UserServices:
    '''
    @marshal_with(UserDto.response)
    def post(self):
        data=request.json
        print(data)
        print((not "namex" in data))
        if not "namex" in data:
    '''        

    # Hace el GET del usuario.
    @staticmethod
    def get_user():
        user = User.current_user()
        if not user:
            return {"message":"Usuario inexistente", "data":user}

        return {"message":"Usuario encontrado", "data":user}

    # Crea el user.
    @staticmethod
    def create_user(name, last_name, role, location, department, birthDate, email, password, validate_password): #nos falta age data["managerPerm"]
        managerPerm=0 # NO tiene permisos de administrador.

        # Valida que el correo sea de Denso para que tenga permisos de administrador.
        if re.search("^\w+(@na\.denso\.com)$", email): # Correo de Denso
            managerPerm=1 # Tiene permisos de administrador.
            #return {"message":"Su dirección de correo no tiene los permisos para acceder.", "success":False}, 400
        print(managerPerm)

        # Generar el código de acceso del usuario
        characters = string.ascii_letters + string.digits # Que el código sea alfanumérico
        code = ''.join(random.choice(characters) for i in range(6)) # Genera el código con una longitud de 6 carácteres.
        print(code) # Imprime el código.

        # Valida que las contraseñas sean iguales.
        if password != validate_password:
            return {"message":"Las contraseñas son diferentes.", "success":False}, 400

        new_user = User(name=name, email=email, password=password, last_name=last_name, role=role, location=location, department=department, managerPerm=managerPerm, birthDate=birthDate, code=code) #nos falta age manager_id=manager_id,

        db.session.add(new_user)
        db.session.commit()

        mensajito = "Usuario creado correctamente con managerPerm "+ str(managerPerm) + " y codigo " + code
        return {"message":mensajito, "success":True}

    # Hace la función de Login
    @staticmethod
    def login(email, password): # Recibe el email y la contraseña
        user = User.query.filter_by(email=email, managerPerm=1).first() #permite iniciar sesion a managers

        # Valida si hay user existente.
        if not user:
            return {"message":"Usuario no encontrado o no es manager", "success":False}, 404
        
        # Valida si la contraseña coincide.
        if not user.check_password(password):
            return {"message":"Contraseña incorrecta", "success":False}, 404

        # Sesiones
        session = Session.open()
        session.set("user_id",user.user_id )
        session.save()

        print(session.get("token"))
        
        return {"message":"Login exitoso. Recargue la página","token":session.get("token"), "success":True} 

    
    @staticmethod
    def get_user_candidate(user_id):
        candidato = User.query.filter_by(user_id=user_id, managerPerm=0).first()
        #candidato = db.session.execute(sqlalchemy.text("CALL SP_ConsultaPerfil(:param)"), {"param":user_id}).fetchall()
        print(candidato)
        if not candidato:
            return {"message":"Candidato no existe o es admin", "success":False}
        return {"message":"Candidato existente", "data":candidato}

    @staticmethod
    def tabla(mylocation, mydepartment):
        print(mylocation + " " + mydepartment)
        #if(len(mylocation)==4): #MTY% -- like
        #    candidato = db.session.execute(sqlalchemy.text("CALL SP_ConsultaLikeLocation(:param)"), {"param":mylocation}).fetchall()
        #else: #MTY Departamento
        if(mylocation=="-" and mydepartment=="-"): #busqueda global
            candidato = User.query.filter_by(managerPerm=0).all()
        elif(mylocation=="-"):
            candidato = User.query.filter_by(department=mydepartment, managerPerm=0).all()
        elif(mydepartment=="-"):
            candidato = User.query.filter_by(location=mylocation, managerPerm=0).all()
        else:
            candidato = User.query.filter_by(location=mylocation, department=mydepartment, managerPerm=0).all()
        print(candidato)
        return candidato#{"message":"Candidatos de locacion dados", "data":candidato}

    @staticmethod
    def kpi(mylocation, mydepartment):
        role = db.session.execute(sqlalchemy.text("CALL SP_ModaRole(:param , :param2)"), {"param":mylocation , "param2":mydepartment}).scalar()
        minigame = db.session.execute(sqlalchemy.text("CALL SP_AvgMinigame(:param , :param2)"), {"param":mylocation , "param2":mydepartment}).scalar()
        psicometrico = db.session.execute(sqlalchemy.text("CALL SP_AvgPsicometrico(:param , :param2)"), {"param":mylocation , "param2":mydepartment}).scalar()
        
        print(str(role) +" "+ str(minigame) +" "+ str(psicometrico))
        return{
        "moda_carrera":role,
        "media_videojuego":minigame,
        "media_psicometrico":psicometrico
        }

    @staticmethod
    def unity(mycode):
        candidato = User.query.filter_by(code=mycode, managerPerm=0).first()
        print(candidato)
        if not candidato:
            return False
        return candidato