from database import db
from sqlalchemy.orm import relationship, backref

# Recrear la modelación que se tiene de las bases de datos en MySQL.

class Partida(db.Model):
    __tablename__ = "partida"
    par_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # a quitarlos
    #email = db.Column(db.String(255), nullable=True)

    #asesor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #asesor = relationship("User", backref=backref("candidatos", uselist=True))
    
    # nuevos
    player_id = db.Column(db.Integer, db.ForeignKey("user.user_id")) #user
    player = relationship("User", backref=backref("partidas", uselist=True))

    game_id = db.Column(db.Integer, db.ForeignKey("game.game_id"))
    game = relationship("Game", backref=backref("partidas", uselist=True))

    score = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)

    timeStamp = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(255), nullable=True)

     # En pocas palabras, la función de relación es una forma conveniente para que sqlalchemy llame entre relaciones, y el parámetro backref proporciona una declaración de referencia inversa para la relación.
    
    # backref agrega una columna 

    # uselist
    # A boolean that indicates if this property should be loaded as a list or a scalar. In most cases, this value is determined automatically by relationship() at mapper configuration time, based on the type and direction of the relationship - one to many forms a list, many to one forms a scalar, many to many is a list. If a scalar is desired where normally a list would be present, such as a bi-directional one-to-one relationship, set relationship.uselist to False.

    # The relationship.uselist flag is also available on an existing relationship() construct as a read-only attribute, which can be used to determine if this relationship() deals with collections or scalar attributes:


