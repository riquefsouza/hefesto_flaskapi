from app import app
from app.admin.models.AdmParemeter import AdmParemeter
from app.admin.schemas.AdmParemeterSchema import admParemeter_schema, admParemeter_schemaMany
from app.admin.schemas.AdmParemeterForm import AdmParemeterForm
from app.admin.services.AdmParemeterService import AdmParemeterService
from flask import request, jsonify

service = AdmParemeterService()

URL = app.config['API_ROOT'] + '/admParemeter'

@app.route(URL, methods=["GET"])
def admParemeter_findAll():
    listaParemeters = service.findAll()
    listaDTO = admParemeter_schemaMany.dump(listaParemeters)
    return jsonify(listaDTO), 200

@app.route(URL + '/<id>', methods=["GET"])
def admParemeter_findById(id: int):
    admParemeter = service.findById(id)
    if admParemeter!=None:
        return admParemeter_schema.jsonify(admParemeter), 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
def admParemeter_save():
    body = request.json
    form: AdmParemeterForm = AdmParemeterForm(body)
    admParemeter = service.save(form)
    if admParemeter!=None:
        return admParemeter_schema.jsonify(admParemeter), 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
def admParemeter_update(id: int):
    body = request.json
    form: AdmParemeterForm = AdmParemeterForm(body)
    admParemeter = service.update(id, form)
    if admParemeter!=None:
        return admParemeter_schema.jsonify(admParemeter), 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
def admParemeter_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


