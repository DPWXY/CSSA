from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from pymysql import IntegrityError

from exts import db
from models.user import UserModel

user_bp = Blueprint("user", __name__)
api = Api(user_bp)


class User(Resource):
    def get(self):

        return jsonify(UserModel.query.all())

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, location='form',
                            required=True)
        parser.add_argument('password', type=str, location='form',
                            required=True)
        parser.add_argument('age', type=int, location='form', required=True)
        args = parser.parse_args()  # 字典
        user = UserModel(username=args.username, password=args.password,
                         age=args.age)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            db.session.flush()
            return 'failed', 409
        return 'success'

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, location='form',
                            required=True)
        args = parser.parse_args()

        UserModel.query.filter_by(username=args['username']).delete()
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            db.session.flush()
            return "failed", 409
        return 'Success'

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, location='form',
                            required=True)
        parser.add_argument('password', type=str, location='form',
                            required=True)
        parser.add_argument('age', type=int, location='form', required=True)
        args = parser.parse_args()
        user = UserModel(username=args.username, password=args.password,
                         age=args.age)

        one = UserModel.query.filter_by(username=args['username']).first()
        one.username = args['username']
        one.password = args['password']
        one.age = args['age']
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            db.session.flush()
            return "failed", 409
        return 'Success'


class UserOne(Resource):
    def get(self, user_id):
        return user_id


api.add_resource(User, '/user')
api.add_resource(UserOne, '/user/<int:user_id>')
