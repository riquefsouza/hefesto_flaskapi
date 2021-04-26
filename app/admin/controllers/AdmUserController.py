from app import app
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserSchema import admUser_schema, admUser_schemaMany
from app.admin.schemas.AdmUserForm import AdmUserForm
from app.admin.services.AdmUserService import AdmUserService
from flask import request, jsonify

service = AdmUserService()

URL = app.config['API_ROOT'] + '/admUser'

@app.route(URL, methods=["GET"])
def admUser_findAll():
    listaUsers = service.findAll()
    #listaDTO = AdmUserDTO.list_to_json(listaUsers)
    listaDTO = admUser_schemaMany.dump(listaUsers)
    #return listaDTO, 200
    return jsonify(listaDTO), 200

@app.route(URL + '/<id>', methods=["GET"])
def admUser_findById(id: int):
    admUser = service.findById(id)
    if admUser!=None:
        #dto = AdmUserDTO(admUser)
        #return dto.to_json(), 200
        return admUser_schema.jsonify(admUser), 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
def admUser_save():
    #search = request.args.get("search")
    #email = request.form.get('email')
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    admUser = service.save(form)
    if admUser!=None:
        #dto = AdmUserDTO(admUser)
        #return dto.to_json(), 201
        return admUser_schema.jsonify(admUser), 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
def admUser_update(id: int):
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    admUser = service.update(id, form)
    if admUser!=None:
        #dto = AdmUserDTO(admUser)
        #return dto.to_json(), 200
        return admUser_schema.jsonify(admUser), 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
def admUser_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


