from app import app
from flask import request
from uuid import uuid4

from db import crops

@app.get('/crops')
def cropList():
  return {'crops':crops}

@app.get('/crops/<crop_name>')
def cropSpec(crop_name):
  try:
    return {f'{crop_name}':crops[crop_name]},200
  except KeyError:
    return {"message" : "Invalid crop"},400

@app.post('/crops')
def addCrop(cropName):
  if cropName not in list(crops):
    json_body=request.get_json()
    crops[cropName]=json_body
    return{'notice':f'{json_body["a-name"]} added to list'},201
  return {"message" : f"{cropName} already in database"},400

@app.put('/crops/<crop_name>')
def updateCrop(crop_name):
  pass


@app.delete('/crops')
def deleteCrop():
  pass