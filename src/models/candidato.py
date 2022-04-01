from database import db
from sqlalchemy.orm import relationship, backref


class Candidato(db.Model):
    __tablename__ = "candidato"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=True)

    asesor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    asesor = relationship("User", backref=backref("candidatos", uselist=True))
    
    




