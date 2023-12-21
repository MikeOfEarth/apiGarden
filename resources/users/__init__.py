from flask_smorest import Blueprint

bp = Blueprint('users',__name__, description="Operations for Users", url_prefix='/users')
from . import routes