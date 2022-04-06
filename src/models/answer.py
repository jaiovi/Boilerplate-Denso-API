from database import db
from sqlalchemy.orm import relationship, backref


class Answer(db.Model):
    __tablename__ = "answer"
    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(255), nullable=True)

    questionFk_id = db.Column(db.Integer, db.ForeignKey("question.question_id"))
    question = relationship("Questions", backref=backref("answers", uselist=True))

    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    user = relationship("Users", backref=backref("users", uselist=True))