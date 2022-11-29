from flask import Flask, request
import json
from blueprints.user_blueprint import user_bp
from blueprints.product_blueprint import product_bp
import config

app = Flask(__name__)

app.config.from_object(config)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.route("/user/<user_id>", methods=['GET'])
# def user2(user_id):
#     with open('user.json', 'r') as f:
#         db = json.load(f)
#     if request.method == "GET":
#         for i in range(len(db["data"])):
#             if db["data"][i]["user_id"] == int(user_id):
#                 return db["data"][i]
#         return "Not found"


# @app.route("/user", methods=['GET', 'POST', 'PUT', 'DELETE'])
# def user():
#     with open('user.json', 'r') as f:
#         db = json.load(f)
#     if request.method == "GET":
#         return db
#     elif request.method == "POST":
#         new = {
#             "user_id": int(request.form["user_id"]),
#             "gender": int(request.form["gender"]),
#             "username": request.form["username"],
#             "age": int(request.form["age"]),
#         }
#         db["data"].append(new)
#         with open('user.json', 'w') as f:
#             json.dump(db, f)
#         return db
#     elif request.method == "PUT":
#         for each in db["data"]:
#             if each["user_id"] == int(request.form["user_id"]):
#                 each["gender"] = int(request.form["gender"])
#                 each["username"] = request.form["username"]
#                 each["age"] = int(request.form["age"])
#         with open('user.json', 'w') as f:
#             json.dump(db, f)
#         return "Success"
#     elif request.method == "DELETE":
#         for i in range(len(db["data"])):
#             if db["data"][i]["user_id"] == int(request.form["user_id"]):
#                 del db["data"][i]
#                 break
#         with open('user.json', 'w') as f:
#             json.dump(db, f)
#         return db
#
#
# @app.route("/product", methods=['GET', 'POST', 'PUT', 'DELETE'])
# def product():
#     with open('user.json', 'r') as f:
#         db = json.load(f)
#     return db


if __name__ == '__main__':
    app.run(debug=True)
