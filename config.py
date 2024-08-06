import secrets


class Config:
    SECRET_KEY = secrets.token_hex(32)
    JWT_SECRET_KEY = secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = "sqlite:///auth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
