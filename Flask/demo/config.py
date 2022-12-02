import os
import classified

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# MySQL 数据库
DB_USERNAME = "root"
DB_PASSWORD = classified.DB_PASSWORD
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "lol"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}charset=utf8".format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

# SQLALCHEMY配置
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
