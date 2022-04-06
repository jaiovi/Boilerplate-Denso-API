from database import db
from sqlalchemy.orm import relationship, backref


class Test(db.Model):
    __tablename__ = "test"
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    testName = db.Column(db.String(255), nullable=True)