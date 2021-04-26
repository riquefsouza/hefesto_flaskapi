from app import app
from app.admin.models.AdmParemeterCategory import AdmParemeterCategory
from app.admin.schemas.AdmParemeterCategorySchema import admParemeterCategory_schema, admParemeterCategory_schemaMany
from app.admin.schemas.AdmParemeterCategoryForm import AdmParemeterCategoryForm
from app.admin.services.AdmParemeterCategoryService import AdmParemeterCategoryService
from flask import request, jsonify

service = AdmParemeterCategoryService()

URL = app.config['API_ROOT'] + '/admParemeterCategory'

@app.route(URL, methods=["GET"])
def admParemeterCategory_findAll():
    listaParemeterCategorys = service.findAll()
    listaDTO = admParemeterCategory_schemaMany.dump(listaParemeterCategorys)
    return jsonify(listaDTO), 200

@app.route(URL + '/<id>', methods=["GET"])
def admParemeterCategory_findById(id: int):
    admParemeterCategory = service.findById(id)
    if admParemeterCategory!=None:
        return admParemeterCategory_schema.jsonify(admParemeterCategory), 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
def admParemeterCategory_save():
    body = request.json
    form: AdmParemeterCategoryForm = AdmParemeterCategoryForm(body)
    admParemeterCategory = service.save(form)
    if admParemeterCategory!=None:
        return admParemeterCategory_schema.jsonify(admParemeterCategory), 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
def admParemeterCategory_update(id: int):
    body = request.json
    form: AdmParemeterCategoryForm = AdmParemeterCategoryForm(body)
    admParemeterCategory = service.update(id, form)
    if admParemeterCategory!=None:
        return admParemeterCategory_schema.jsonify(admParemeterCategory), 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
def admParemeterCategory_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


