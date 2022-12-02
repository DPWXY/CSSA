from dataclasses import dataclass
import shortuuid as shortuuid
from werkzeug.security import generate_password_hash\

from exts import db

@dataclass
class UserModel(db.Model):
    # 这个类有哪些属性
    id: str
    username: str
    password: str
    join_time: str
    age: int

    # 对应着表的结构
    __tablename__ = "users"
    id = db.Columns(db.String(100), primary_key=True, default=shortuuid.uuid)
    username = db.Columns(db.String(50), nullable=False)
    _password = db.Columns(db.String(200), nullable=False)
    join_time = db.Columns(db.DataTime, default=datetime.now)
    age = db.Columns(db.Integer)

    def __init__(self, *args, **kwargs):
        if "password" in kwargs:
            self.password = kwargs['password']
            kwargs.pop('password')
        super(UserModel, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = generate_password_hash(new_password)



