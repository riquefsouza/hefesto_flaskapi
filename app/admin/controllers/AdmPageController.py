from app import app
from app.admin.models.AdmPage import AdmPage
from app.admin.schemas.AdmPageSchema import admPage_schema, admPage_schemaMany
from app.admin.schemas.AdmPageForm import AdmPageForm
from app.admin.services.AdmPageService import AdmPageService
from flask import request, jsonify

service = AdmPageService()

URL = app.config['API_ROOT'] + '/admPage'

@app.route(URL, methods=["GET"])
def admPage_findAll():
    listaPages = service.findAll()
    return listaPages, 200

@app.route(URL + '/<id>', methods=["GET"])
def admPage_findById(id: int):
    admPage = service.findById(id)
    if admPage!=None:
        return admPage, 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
def admPage_save():
    body = request.json
    form: AdmPageForm = AdmPageForm(body)
    admPage = service.save(form)
    if admPage!=None:
        return admPage, 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
def admPage_update(id: int):
    body = request.json
    form: AdmPageForm = AdmPageForm(body)
    admPage = service.update(id, form)
    if admPage!=None:
        return admPage, 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
def admPage_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


