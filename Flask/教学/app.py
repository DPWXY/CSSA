from flask import Flask, send_file, request
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/lol/<user_id>")
# def lol(user_id):
#     # return send_file(os.path.join( os.path.realpath(os.path.dirname(__file__)), "assets/", "fluorescent_sea.JPG"))
#     return user_id

# RESTFUL
# 没有参数的GET请求获取全部数据
# 有参数的GET请求获取单一数据
# POST请求是新增
# DELETE 请求是删除
# PUT 请求是修改

@app.route("/lol", methods=['GET', 'POST', 'PUT', 'DELETE'])
def lol(user_id):
    table = {
        "a": {
            "user": 1,
            "age": 2
        },
        "b": {
            "user": 2,
            "age": 3
        }
    }
    if request.method == "GET":
        # return request.headers["a"]
        # return request.form["b"]
        return table
    elif request.method == "POST":
        # return "post"
        table["3"] = {
            "user": request.form["user"],
            "age": request.form["age"]
        }
    elif request.method == "PUT":
        table[request.form["user_id"]] = {
            "user": request.form["user"],
            "age": request.form["age"]
        }
    elif request.method == "DELETE":
        del table[request.form["user_id"]]


@app.route("/lol/<user_id>", methods=['GET'])
def lol1(user_id):
    table = {
        "a": {
            "user": 1,
            "age": 2
        },
        "b": {
            "user": 2,
            "age": 3
        }
    }
    if request.method == "GET":
        return table[user_id]


if __name__ == '__main__':
    app.run(debug=True)
