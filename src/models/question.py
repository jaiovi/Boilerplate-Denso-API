from database import db
from sqlalchemy.orm import relationship, backref


class Question(db.Model):
    __tablename__ = "question"
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(255), nullable=True)

    game_id = db.Column(db.Integer, db.ForeignKey("game.game_id"))
    game = relationship("Game", backref=backref("questions", uselist=True))
    