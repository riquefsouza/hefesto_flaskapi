from app import app
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserSchema import admUser_schema, admUser_schemaMany
from app.admin.schemas.AdmUserForm import AdmUserForm
from app.admin.services.AdmUserService import AdmUserService
from flask import request, jsonify
from flask_jwt_extended import jwt_required

service = AdmUserService()

URL = app.config['API_ROOT'] + '/admUser'

@app.route(URL, methods=["GET"])
@jwt_required()
def admUser_findAll():
    listaUsers = service.findAll()
    return listaUsers, 200

@app.route(URL + '/<id>', methods=["GET"])
@jwt_required()
def admUser_findById(id: int):
    admUser = service.findById(id)
    if admUser!=None:
        #return admUser_schema.jsonify(admUser), 200
        return admUser, 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
@jwt_required()
def admUser_save():
    #search = request.args.get("search")
    #email = request.form.get('email')
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    admUser = service.save(form)
    if admUser!=None:
        #return admUser_schema.jsonify(admUser), 201
        return admUser, 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
@jwt_required()
def admUser_update(id: int):
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    admUser = service.update(id, form)
    if admUser!=None:
        #return admUser_schema.jsonify(admUser), 200
        return admUser, 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
@jwt_required()
def admUser_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


