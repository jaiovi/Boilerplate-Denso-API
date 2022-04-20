
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from src.controllers.user_controller import UserController, UserControllerFindUser, UserLoginController
from flask_migrate import Migrate
from database import db, bcrypt

# endpoint,: url que va a llaamar a ese pedazo de código. Por jejemplo: www.maquinaJD.0001/Marcador
# cuando se pone marcador, se que ese pedazo de código es el que se debe de ejecutar
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@127.0.0.1/DensoDB"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

CORS(app)
api = Api(app)
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db, directory="./database/migrations")




api.add_resource(UserController, "/user")
api.add_resource(UserLoginController, "/user/login")

#incio de clase 6 abril
#api.add_resource(UserControllerFindUser, "/user/search/<user_id>")




"""
app
    - models
    - services
    - controllers
application.py
"""