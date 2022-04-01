import pickle
import datetime
import uuid
from database import db, app_key
from itsdangerous import want_bytes
import jwt

class Session(db.Model):
    __tablename__ = "session"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(255), unique=True)
    data = db.Column(db.LargeBinary)
    expirataion = db.Column(db.DateTime)

    data_ = {}

    def get(self, key):
        return self.data_.get(key, False )
    
    def set(self, key, value):
        self.data_[key] = value

    @staticmethod
    def open(token=None):
        if not token:
            sid = str(uuid.uuid4())
            new_session = Session(token=sid, expirataion=datetime.datetime.utcnow() + datetime.timedelta(days=5,seconds=3))
            values = pickle.dumps(dict())
            new_session.data = values
            token_crypt = Session.encrypt_token(sid)
            new_session.data_["token"] = token_crypt
            db.session.add(new_session)
            db.session.commit()
            return new_session
        else:
            token_decrypt = Session.decrypt_token(token)
            if token_decrypt:
                session = Session.query.filter_by(token=token_decrypt).first()
              
                if session and session.expirataion <= datetime.datetime.utcnow():
                    db.session.delete(session)
                    db.session.commit()
                    return None
                
                if session:
                    values = session.data
                    session.data_ = pickle.loads(want_bytes(values))
                    return session
            return None
    
    def save(self):
        values = pickle.dumps(dict(self.data_))
        self.data = values
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def encrypt_token(sid):
        try:
            payload = {"sid": sid}
            return jwt.encode(
                payload,
                key=app_key,
                algorithm="HS256"
            )
        except Exception as e:
            print(e)
            return e
    
    @staticmethod
    def decrypt_token(token):
        try:
           payload = jwt.decode(token, app_key, algorithms="HS256")
           return payload["sid"]
        except Exception as e:
            print(e)
            return e