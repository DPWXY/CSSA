from flask import Flask
from blueprints.user_blueprint import user_bp
from exts import db
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(user_bp)
db.init_app(app)
migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run()
