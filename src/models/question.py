from database import db
from sqlalchemy.orm import relationship, backref


class Question(db.Model):
    __tablename__ = "question"
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(255), nullable=True)

    testFK_id = db.Column(db.Integer, db.ForeignKey("test.test_id"))
    test = relationship("Test", backref=backref("question", uselist=True))
    