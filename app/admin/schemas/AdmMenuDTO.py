from app.admin.models.AdmMenu import AdmMenu
from app.admin.models.AdmPage import AdmPage
from app.admin.schemas.AdmPageDTO import AdmPageDTO
import json
from typing import List
from flask import jsonify


class AdmMenuDTO:
    id: int
    description: str
    idMenuParent: int
    idPage: int
    order: int
    #admMenuParent: AdmMenuDTO
    admPage: AdmPageDTO
    url: str
    subMenus = []

    def __init__(self, admMenu: AdmMenu):
        self.id = admMenu.id
        self.description = admMenu.description
        self.idMenuParent = admMenu.idMenuParent
        self.idPage = admMenu.idPage
        self.order = admMenu.order
        #self.admMenuParent = AdmMenuDTO(admMenu.admMenuParent)
        #self.admPage = AdmPageDTO(admMenu.admPage)
        self.url = ""
        self.subMenus = []

    def to_json(self):
        #return json.dumps(self.__dict__)
        return jsonify(self.__dict__)
    
    @staticmethod
    def list_to_json(lista: List[AdmMenu]):
        listaDTO = []
        for item in lista:
            dto = AdmMenuDTO(item)
            listaDTO.append(dto.__dict__)
        #return json.dumps(listaDTO)
        return jsonify(listaDTO)