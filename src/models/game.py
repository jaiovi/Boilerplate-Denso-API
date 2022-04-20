from database import db
from sqlalchemy.orm import relationship, backref


class Game(db.Model):
    __tablename__ = "game"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gameName = db.Column(db.String(255), nullable=True)
    habilidad = db.Column(db.String(255), nullable=True)

    nivelAvanzado = db.Column(db.Integer, nullable=True)
    nivelProceso = db.Column(db.Integer, nullable=True)
    nivelInicial = db.Column(db.Integer, nullable=True)

    test_id = db.Column(db.Integer, db.ForeignKey("test.test_id"))
    test = relationship("Test", backref=backref("games", uselist=True))
    