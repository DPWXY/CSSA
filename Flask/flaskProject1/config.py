import os
import classified

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

DB_USERNAME = "root"
DB_PASSWORD = classified.DB_PASSWORD
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "smallshrimp"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(DB_USERNAME,
                                                              DB_PASSWORD,
                                                              DB_HOST, DB_PORT,
                                                              DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
