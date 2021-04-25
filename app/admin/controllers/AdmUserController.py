from app import app
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserDTO import AdmUserDTO
from app.admin.schemas.AdmUserForm import AdmUserForm
from app.admin.services.AdmUserService import AdmUserService
from flask import request

service = AdmUserService()

URL = '/api/v1/admUser'

@app.route(URL, methods=["GET"])
def findAll():
    listaUsers = service.findAll()
    listaDTO = AdmUserDTO.list_to_json(listaUsers);
    return listaDTO, 200

@app.route(URL + '/<id>', methods=["GET"])
def findById(id: int):
    admUser = service.findById(id)
    dto = AdmUserDTO(admUser)
    return dto.to_json(), 200

@app.route(URL, methods=["POST"])
def save():
    #search = request.args.get("search")
    #email = request.form.get('email')
    body = request.json
    form: AdmUserForm = AdmUserForm(body)
    newAdmUser = service.save(form)
    return {
        "admUser_id": newAdmUser.id
    }

@app.route(URL + '/<id>', methods=["PUT"])
def update(id: int):
    body = request.json
    form: AdmUserForm = AdmUserForm(body)

    admUser = service.update(id, form)
    dto = AdmUserDTO(admUser)
    return dto.to_json()

@app.route(URL + '/<id>', methods=["DELETE"])
def delete(id: int):
    bOk: bool = service.delete(id)
    return {"success": bOk}


