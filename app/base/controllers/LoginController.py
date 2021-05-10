from app import app
from app.admin.services.AdmUserService import AdmUserService
from app.base.schemas.UserDTO import UserDTO
from app.base.schemas.TokenDTO import TokenDTO
from app.base.schemas.LoginForm import LoginForm
from app.base.services.AuthHandlerService import AuthHandlerService
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta

service = AdmUserService()
authHandler = AuthHandlerService()

URL = '/auth'

@app.route(URL, methods=["POST"])
def login():
    body = request.json
    loginForm: LoginForm = LoginForm(body)

    try:
        if (loginForm != None and loginForm.login != None and loginForm.password != None):
            admUser = service.authenticate(loginForm.login, loginForm.password)
            if admUser!=None:
                user = UserDTO()
                user.id = admUser.id
                user.name = admUser.name
                user.email = admUser.email

                dto = authHandler.encode_token(user)      
        
                return dto.to_json(), 200
            else:
                print(f'Authentication failed for user {loginForm.login}')
                print('No token generated')
                return "{ 'message': 'Authentication failed for user " + loginForm.login + "' }", 401
        else:    
            return "", 400
    except Exception as e:
        return "", 400
