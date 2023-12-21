from app import app
from flask import request

from db import users

@app.get('/users')
def userList():
    return {'users':users}

@app.post('/users')
def addUser(username):
    json_body=request.get_json()
    users[username]=json_body
    return{'notice':f'{username} added to list'},201

@app.put('/users')
def updateProfile():
  return

@app.delete('/users')
def deleteUser():
  pass
