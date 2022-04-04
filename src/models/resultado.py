from database import db
from sqlalchemy.orm import relationship, backref


class Resultado(db.Model):
    __tablename__ = "resultado"
    res_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # a quitarlos
    #email = db.Column(db.String(255), nullable=True)

    #asesor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #asesor = relationship("User", backref=backref("candidatos", uselist=True))
    
    # nuevos
    player_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    player = relationship("User", backref=backref("resultados", uselist=True))
    game = db.Column(db.String(255), nullable=True)
    score = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)

