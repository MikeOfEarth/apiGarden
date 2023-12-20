from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users={
   "oldMacDon":{
      "name":"Tobias McDonald",
      "email":"runch1ckenrun@gmail.com",
      "password":"funkyTown"
    }
}

@app.get('/users')
def userList():
    return {'users':users}

@app.post('/users')
def addUser(username):
    json_body=request.get_json()
    crops[username]=json_body
    return{'notice':f'{username} added to list'},201

@app.put('/users')
def updateProfile():
  return

@app.delete('/users')
def deleteUser():
  pass

# userside
# ------------------------------------------------------------------------------------------------------------------------
# cropside

crops={
    "tomato":{
        "seasons":["spring","summer","fall"],
        "light-preference":"full",
        "grow-time":10,
        "companions":["basil","marigold"],
        "repeat-harvest":4,
        "per-harvest":1
    },
    "lettuce":{
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
    101:{
        "grid-value-x":1,
        "grid-value-y":1,
        "owner":"oldMacDon",
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
def tillPlot(gridNum):
    json_body=request.get_json()
    plots[gridNum]=json_body
    return{'notice':f'{json_body["grid-value"]} has been tilled'},201

@app.put('/plots')
def plantPlot():
  return

@app.delete('/plots')
def harvestPlot():
  pass