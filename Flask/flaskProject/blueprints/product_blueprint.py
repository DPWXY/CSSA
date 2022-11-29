import os
import json

from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from config import SITE_ROOT

product_bp = Blueprint("product", __name__)
api = Api(product_bp)


class Product(Resource):
    def get(self):
        return 'product get'


api.add_resource(Product, '/product')