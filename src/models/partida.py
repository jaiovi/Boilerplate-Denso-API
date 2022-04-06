from database import db
from sqlalchemy.orm import relationship, backref


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

    gameFK_id = db.Column(db.Integer, db.ForeignKey("game.game_id"))
    game = relationship("Game", backref=backref("partidas", uselist=True))

    score = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)

    timeStamp = db.Column(db.Date, nullable=True)
    status = name = db.Column(db.String(255), nullable=True)
