from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User, db

parser = reqparse.RequestParser()
parser.add_argument("username", required=False)
parser.add_argument("email", required=False)
parser.add_argument("password", required=False)
parser.add_argument("current_password", required=False)


class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()
        if User.query.filter_by(username=data["username"]).first():
            return {"message": "User already exists"}, 400
        hashed_password = generate_password_hash(
            data["password"], method="pbkdf2:sha256"
        )
        new_user = User(
            username=data["username"], password=hashed_password, email=data["email"]
        )
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully"}, 201


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = User.query.filter_by(username=data["username"]).first()
        if not user or not check_password_hash(user.password, data["password"]):
            return {"message": "Invalid credentials"}, 401
        access_token = create_access_token(
            identity={"id": user.id, "username": user.username, "email": user.email}
        )
        return jsonify(access_token=access_token)


class UserUpdate(Resource):
    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user["id"]).first()

        if not user:
            return {"message": "User not found"}, 404

        data = parser.parse_args()
        if data["username"]:
            user.username = data["username"]
        if data["email"]:
            user.email = data["email"]
        if data["password"]:
            if not check_password_hash(user.password, data["current_password"]):
                return {"message": "Current password is incorrect"}, 400
            user.password = generate_password_hash(
                data["password"], method="pbkdf2:sha256"
            )

        db.session.commit()
        access_token = create_access_token(
            identity={"id": user.id, "username": user.username, "email": user.email}
        )
        return jsonify(
            access_token=access_token, message="User information updated successfully"
        )

    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user["id"]).first()

        if not user:
            return {"message": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User account deleted successfully"}, 200


class UserProfile(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user["id"]).first()
        if not user:
            return {"message": "User not found"}, 404
        return {"username": user.username, "email": user.email}, 200
