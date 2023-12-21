from flask import Flask
from flask_smorest import Api
from Config import Config
app = Flask(__name__)

app.config.from_object(Config)
api=Api(app)

from resources.crops import bp as crops_bp
api.register_blueprint(crops_bp)

from resources.plots import bp as plots_bp
api.register_blueprint(plots_bp)

from resources.users import bp as users_bp
api.register_blueprint(users_bp)