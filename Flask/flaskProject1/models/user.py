from dataclasses import dataclass
from datetime import datetime

import shortuuid
from werkzeug.security import generate_password_hash
from exts import db


@dataclass
class UserModel(db.Model):
    id: str
    username: str
    password: str
    join_time: str
    age: int

    __tablename__ = 'users'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now())
    age = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs["password"]
            kwargs.pop("password")
        super(UserModel, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = generate_password_hash(new_password)
