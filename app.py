from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

crops={
    "1":{
        "a-name":"tomato",
        "seasons":["spring","summer","fall"],
        "light-preference":"full",
        "grow-time":10,
        "companions":["basil","marigold"],
        "repeat-harvest":4,
        "per-harvest":1
    },
    "2":{
        "a-name":"lettuce",
        "seasons":["spring","fall"],
        "light-preference":"part-shade",
        "grow-time":7,
        "companions":["carrot","radish","strawberry"],
        "repeat-harvest":2,
        "per-harvest":1
    }
}

@app.get('/crops')
def cropList():
    return {'crops':list(crops.values())}

@app.post('/crops')
def addCrop():
    json_body=request.get_json()
    crops[uuid4()]=json_body
    return{'notice':f'{json_body["a-name"]} added to list'},201

@app.put('/crops')
def updateCrop():
  return

@app.delete('/crops')
def deleteCrop():
  pass

# cropside
# ------------------------------------------------------------------------------------------------------------------------
# plotside

plots={
    1:{
       "grid-value":'1,1',
        "light":"full",
        "crop":None,
        "watered":False,
        "tilled":True,
        "fertilizer":None
    }
}

@app.get('/plots')
def plotList():
    return {'plots':list(plots.values())}

@app.post('/plots')
def tillPlot():
    json_body=request.get_json()
    plots[uuid4()]=json_body
    return{'notice':f'{json_body["grid-value"]} has been tilled'},201

@app.put('/plots')
def plantPlot():
  return

@app.delete('/plots')
def harvestPlot():
  pass