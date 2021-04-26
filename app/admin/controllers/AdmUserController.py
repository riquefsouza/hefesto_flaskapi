from app import app
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserSchema import adm_user_schema, adm_users_schema
from app.admin.schemas.AdmUserDTO import AdmUserDTO
from app.admin.schemas.AdmUserForm import AdmUserForm
from app.admin.services.AdmUserService import AdmUserService
from flask import request, jsonify

service = AdmUserService()

URL = app.config['API_ROOT'] + '/admUser'

@app.route(URL, methods=["GET"])
def findAll():
    listaUsers = service.findAll()
    #listaDTO = AdmUserDTO.list_to_json(listaUsers)
    listaDTO = adm_users_schema.dump(listaUsers)
    #return listaDTO, 200
    return jsonify(listaDTO), 200

@app.route(URL + '/<id>', methods=["GET"])
def findById(id: int):
    admUser = service.findById(id)
    if admUser!=None:
        #dto = AdmUserDTO(admUser)
        #return dto.to_json(), 200
        return adm_user_schema.jsonify(admUser), 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
def save():
    #search = request.args.get("search")
    #email = request.form.get('email')
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    admUser = service.save(form)
    if admUser!=None:
        #dto = AdmUserDTO(admUser)
        #return dto.to_json(), 201
        return adm_user_schema.jsonify(admUser), 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
def update(id: int):
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    admUser = service.update(id, form)
    if admUser!=None:
        #dto = AdmUserDTO(admUser)
        #return dto.to_json(), 200
        return adm_user_schema.jsonify(admUser), 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
def delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


