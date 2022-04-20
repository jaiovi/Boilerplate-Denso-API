from database import db
from sqlalchemy.orm import relationship, backref


class Answer(db.Model):
    __tablename__ = "answer"
    answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scale_num = db.Column(db.Integer, nullable=True)

    question_id = db.Column(db.Integer, db.ForeignKey("question.question_id"))
    question = relationship("Question", backref=backref("answers", uselist=True))

    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    user = relationship("User", backref=backref("users", uselist=True))