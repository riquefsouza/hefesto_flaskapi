from app import app
from app.admin.models.AdmParameter import AdmParameter
from app.admin.schemas.AdmParameterSchema import admParameter_schema, admParameter_schemaMany
from app.admin.schemas.AdmParameterForm import AdmParameterForm
from app.admin.services.AdmParameterService import AdmParameterService
from flask import request, jsonify
from flask_jwt_extended import jwt_required

service = AdmParameterService()

URL = app.config['API_ROOT'] + '/admParameter'

@app.route(URL, methods=["GET"])
@jwt_required()
def admParameter_findAll():
    listaParameters = service.findAll()
    #listaDTO = admParameter_schemaMany.dump(listaParameters)
    #return jsonify(listaDTO), 200
    return listaParameters, 200

@app.route(URL + '/<id>', methods=["GET"])
@jwt_required()
def admParameter_findById(id: int):
    admParameter = service.findById(id)
    if admParameter!=None:
        #return admParameter_schema.jsonify(admParameter), 200
        return admParameter, 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
@jwt_required()
def admParameter_save():
    body = request.json
    form: AdmParameterForm = AdmParameterForm(body)
    admParameter = service.save(form)
    if admParameter!=None:
        #return admParameter_schema.jsonify(admParameter), 201
        return admParameter, 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
@jwt_required()
def admParameter_update(id: int):
    body = request.json
    form: AdmParameterForm = AdmParameterForm(body)
    admParameter = service.update(id, form)
    if admParameter!=None:
        #return admParameter_schema.jsonify(admParameter), 200
        return admParameter, 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
@jwt_required()
def admParameter_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


