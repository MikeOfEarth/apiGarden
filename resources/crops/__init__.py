from flask_smorest import Blueprint

bp = Blueprint('crops',__name__, description="Operations for Crops", url_prefix='/crops')
from . import routes