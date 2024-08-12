import os
import datetime


class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=365)
    SQLALCHEMY_DATABASE_URI = "sqlite:///auth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
