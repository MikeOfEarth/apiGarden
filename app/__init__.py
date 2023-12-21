from flask import Flask

app = Flask(__name__)

from resources.users import routes
from resources.crops import routes
from resources.plots import routes
from db import crops
app.get('/crops')
def cropList():
  return {'crops':list(crops.values())}