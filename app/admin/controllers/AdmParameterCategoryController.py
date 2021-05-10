from app import app
from app.admin.models.AdmParameterCategory import AdmParameterCategory
from app.admin.schemas.AdmParameterCategorySchema import admParameterCategory_schema, admParameterCategory_schemaMany
from app.admin.schemas.AdmParameterCategoryForm import AdmParameterCategoryForm
from app.admin.services.AdmParameterCategoryService import AdmParameterCategoryService
from flask import request, jsonify
from flask_jwt_extended import jwt_required

service = AdmParameterCategoryService()

URL = app.config['API_ROOT'] + '/admParameterCategory'

@app.route(URL, methods=["GET"])
@jwt_required()
def admParameterCategory_findAll():
    listaParameterCategorys = service.findAll()
    listaDTO = admParameterCategory_schemaMany.dump(listaParameterCategorys)
    return jsonify(listaDTO), 200

@app.route(URL + '/<id>', methods=["GET"])
@jwt_required()
def admParameterCategory_findById(id: int):
    admParameterCategory = service.findById(id)
    if admParameterCategory!=None:
        return admParameterCategory_schema.jsonify(admParameterCategory), 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
@jwt_required()
def admParameterCategory_save():
    body = request.json
    form: AdmParameterCategoryForm = AdmParameterCategoryForm(body)
    admParameterCategory = service.save(form)
    if admParameterCategory!=None:
        return admParameterCategory_schema.jsonify(admParameterCategory), 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
@jwt_required()
def admParameterCategory_update(id: int):
    body = request.json
    form: AdmParameterCategoryForm = AdmParameterCategoryForm(body)
    admParameterCategory = service.update(id, form)
    if admParameterCategory!=None:
        return admParameterCategory_schema.jsonify(admParameterCategory), 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
@jwt_required()
def admParameterCategory_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404


