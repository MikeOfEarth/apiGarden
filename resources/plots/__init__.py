from flask_smorest import Blueprint

bp = Blueprint('plots',__name__, description="Operations for Plots", url_prefix='/plots')
from . import routes