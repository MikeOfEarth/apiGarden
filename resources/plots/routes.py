from app import app
from flask import request

from db import *

@app.get('/plots')
def plotList():
    return {'plots':list(plots.values())}

@app.post('/plots')
def tillPlot(gridNum):
  if gridNum not in plots or plots[gridNum]['user']==None:
    json_body=request.get_json()
    plots[gridNum]=json_body
    return{'notice':f'Grid {json_body["grid-value-x"]}x{json_body["grid-value-y"]} has been tilled by {plots[gridNum]["user"]}'},201
  return {'notice':"Plot untillable"},401

@app.put('/plots')
def plantPlot():
  return

@app.delete('/plots')
def harvestPlot():
  pass