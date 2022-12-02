from flask import Flask
from blueprints.user_blueprint import user_bp
from flask_migrate import Migrate
from exts import db
import config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(user_bp)

db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
