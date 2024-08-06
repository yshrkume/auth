from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from resources.user import UserRegister, UserLogin, UserUpdate, UserProfile

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

api = Api(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(UserUpdate, "/update")
api.add_resource(UserProfile, "/profile")

if __name__ == "__main__":
    app.run()
