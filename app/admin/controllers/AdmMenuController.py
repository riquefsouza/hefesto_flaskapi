from app import app
from app.admin.models.AdmMenu import AdmMenu
from app.admin.schemas.AdmMenuSchema import admMenu_schema, admMenu_schemaMany
from app.admin.schemas.AdmMenuForm import AdmMenuForm
from app.admin.services.AdmMenuService import AdmMenuService
from flask import request, jsonify
from typing import List
from flask_jwt_extended import jwt_required

service = AdmMenuService()

URL = app.config['API_ROOT'] + '/admMenu'

@app.route(URL, methods=["GET"])
@jwt_required()
def admMenu_findAll():
    listaMenus = service.findAll()
    #listaDTO = admMenu_schemaMany.dump(listaMenus)
    #return jsonify(listaDTO), 200
    return listaMenus, 200

@app.route(URL + '/<id>', methods=["GET"])
@jwt_required()
def admMenu_findById(id: int):
    admMenu = service.findById(id)
    if admMenu!=None:
        #return admMenu_schema.jsonify(admMenu), 200
        return admMenu, 200
    else:
        return "", 404

@app.route(URL, methods=["POST"])
@jwt_required()
def admMenu_save():
    body = request.json
    form: AdmMenuForm = AdmMenuForm(body)
    admMenu = service.save(form)
    if admMenu!=None:
        #return admMenu_schema.jsonify(admMenu), 201
        return admMenu, 201
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["PUT"])
@jwt_required()
def admMenu_update(id: int):
    body = request.json
    form: AdmMenuForm = AdmMenuForm(body)
    admMenu = service.update(id, form)
    if admMenu!=None:
        #return admMenu_schema.jsonify(admMenu), 200
        return admMenu, 200
    else:
        return "", 404

@app.route(URL + '/<id>', methods=["DELETE"])
@jwt_required()
def admMenu_delete(id: int):
    bOk: bool = service.delete(id)
    if bOk:
        return "", 200
    else:
        return "", 404

@app.route(URL + '/mountMenu', methods=["GET"])
@jwt_required()
def mountMenu():
    body = request.json
    listIdProfile = body
    menuItemDTO = service.mountMenuItem(listIdProfile)
    return menuItemDTO, 200
