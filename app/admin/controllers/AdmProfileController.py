from app import app
from app.admin.models.AdmProfile import AdmProfile
from app.admin.schemas.AdmProfileSchema import admProfile_schema, admProfile_schemaMany
from app.admin.schemas.AdmProfileForm import AdmProfileForm
from app.admin.services.AdmProfileService import AdmProfileService
from flask import request, jsonify
from flask_jwt_extended import jwt_required

service = AdmProfileService()

URL = app.config['API_ROOT'] + '/admProfile'

@app.route(URL, methods=["GET"])
@jwt_required()
def admProfile_findAll():
    listaProfiles = service.findAll()
    #listaDTO = admProfile_schemaMany.dump(listaProfiles)
    #return jsonify(listaDTO), 200
    return listaProfiles, 200

@app.route(URL + '/<id>', methods=["GET"])
@jwt_required()
def admProfile_findById(id: int):
    admProfile = service.findById(id)
    if admProfile!=None:
        #return admProfile_schema.jsonify(admProfile), 200
        return admProfile, 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
@jwt_required()
def admProfile_save():
    body = request.json
    form: AdmProfileForm = AdmProfileForm(body)
    admProfile = service.save(form)
    if admProfile!=None:
        #return admProfile_schema.jsonify(admProfile), 201
        return admProfile, 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
@jwt_required()
def admProfile_update(id: int):
    body = request.json
    form: AdmProfileForm = AdmProfileForm(body)
    admProfile = service.update(id, form)
    if admProfile!=None:
        #return admProfile_schema.jsonify(admProfile), 200
        return admProfile, 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
@jwt_required()
def admProfile_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404

@app.route(URL + '/<pageId>', methods=["GET"])
@jwt_required()
def findProfilesByPage(pageId: int):
    listAdmProfile = service.findProfilesByPage(pageId)
    if listAdmProfile!=None:
        return jsonify(listAdmProfile), 200
    else:
        return "", 404

@app.route(URL + '/<userId>', methods=["GET"])
@jwt_required()
def findProfilesByUser(userId: int):
    listAdmProfile = service.findProfilesByUser(userId)
    if listAdmProfile!=None:
        return jsonify(listAdmProfile), 200
    else:
        return "", 404

