from flask import Flask
from flask_cors import CORS

from app.admin import admin_blueprint
from app.api import api_blueprint
from common.models import db


# 创建app
def create_app(config=None):
    if config is None:
        import config

    app = Flask(__name__)
    print(config)
    app.config.from_object(config)
    db.init_app(app)

    app.register_blueprint(api_blueprint)
    app.register_blueprint(admin_blueprint)

    CORS(app, supports_credentials=True)

    return app
