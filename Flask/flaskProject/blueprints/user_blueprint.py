import os
import json

from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from config import SITE_ROOT

user_bp = Blueprint("user", __name__)
api = Api(user_bp)


def get_db():
    json_url = os.path.join(SITE_ROOT, 'assets', 'user.json')
    with open(json_url, 'r', encoding="utf-8") as f:
        db = json.load(f)
    return db


def write_db(db):
    json_url = os.path.join(SITE_ROOT, 'assets', 'user.json')
    with open(json_url, 'w', encoding='utf-8') as f:
        json.dump(db, f)
    return db


class User(Resource):
    def get(self):
        db = get_db()
        return db['data']

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, location='form', required=True)
        parser.add_argument('username', type=str, location='form', required=True)
        parser.add_argument('gender', type=int, location='form', required=True)
        parser.add_argument('age', type=int, location='form', required=True)
        args = parser.parse_args()
        db = get_db()
        db['data'].append({
            "user_id": args["user_id"],
            "gender": args["gender"],
            "username": args["username"],
            "age": args["age"],
        })
        write_db(db)
        return 'Success'

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, location='form', required=True)
        parser.add_argument('username', type=str, location='form')
        parser.add_argument('gender', type=int, location='form')
        parser.add_argument('age', type=int, location='form')
        args = parser.parse_args()
        db = get_db()
        for i in db['data']:
            if i["user_id"] == args['user_id']:
                for k, v in args.items():
                    if k == 'user_id':
                        continue
                    else:
                        i[k] = v
        write_db(db)
        return 'Success'

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, location='form', required=True)
        args = parser.parse_args()  # 字典
        db = get_db()
        for i in db["data"]:
            if i['user_id'] == args['user_id']:
                db["data"].remove(i)
                break
        write_db(db)
        return 'Success'


class UserGetOne(Resource):
    def get(self, user_id):
        db = get_db()
        for i in range(len(db["data"])):
            if db["data"][i]["user_id"] == int(user_id):
                return db["data"][i]
        return "Not found"


api.add_resource(User, "/user")
api.add_resource(UserGetOne, "/user/<int:user_id>")