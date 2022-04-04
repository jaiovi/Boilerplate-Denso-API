from database import db, bcrypt
from flask import request

from .session import Session


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    #password = db.Column(db.String(255), nullable=True)
    password_hash = db.Column(db.String(255), nullable=True)

    last_name = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    managerPerm = db.Column(db.Boolean, nullable=True)

    @property
    def password(self):
       raise AttributeError("password: write-only field")

    @password.setter
    def password(self, value):
        self.password_hash = bcrypt.generate_password_hash(value).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def current_user():
        auth_token = request.headers.get('Authorization')
        print(auth_token)

       
        if auth_token:
            session = Session.open(auth_token)
            
            if session:
                user = User.query.filter_by(id=session.get("user_id")).first()
                return user
            return None
        else:
            return None
