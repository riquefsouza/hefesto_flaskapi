from app import app
from app.admin.models.AdmProfile import AdmProfile
from app.admin.schemas.AdmProfileSchema import admProfile_schema, admProfile_schemaMany
from app.admin.schemas.AdmProfileForm import AdmProfileForm
from app.admin.services.AdmProfileService import AdmProfileService
from flask import request, jsonify

service = AdmProfileService()

URL = app.config['API_ROOT'] + '/admProfile'

@app.route(URL, methods=["GET"])
def admProfile_findAll():
    listaProfiles = service.findAll()
    listaDTO = admProfile_schemaMany.dump(listaProfiles)
    return jsonify(listaDTO), 200

@app.route(URL + '/<id>', methods=["GET"])
def admProfile_findById(id: int):
    admProfile = service.findById(id)
    if admProfile!=None:
        return admProfile_schema.jsonify(admProfile), 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
def admProfile_save():
    body = request.json
    form: AdmProfileForm = AdmProfileForm(body)
    admProfile = service.save(form)
    if admProfile!=None:
        return admProfile_schema.jsonify(admProfile), 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
def admProfile_update(id: int):
    body = request.json
    form: AdmProfileForm = AdmProfileForm(body)
    admProfile = service.update(id, form)
    if admProfile!=None:
        return admProfile_schema.jsonify(admProfile), 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
def admProfile_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404

@app.route(URL + '/<pageId>', methods=["GET"])
def findProfilesByPage(pageId: int):
    listAdmProfile = service.findProfilesByPage(pageId)
    if listAdmProfile!=None:
        return jsonify(listAdmProfile), 200
    else:
        return "", 404

@app.route(URL + '/<userId>', methods=["GET"])
def findProfilesByUser(userId: int):
    listAdmProfile = service.findProfilesByUser(userId)
    if listAdmProfile!=None:
        return jsonify(listAdmProfile), 200
    else:
        return "", 404

