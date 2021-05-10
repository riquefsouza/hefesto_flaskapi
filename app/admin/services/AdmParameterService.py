from app import db
from app.admin.models.AdmParameter import AdmParameter
from app.admin.schemas.AdmParameterForm import AdmParameterForm
from app.admin.schemas.AdmParameterDTO import AdmParameterDTO
from app.admin.schemas.AdmParameterCategoryDTO import AdmParameterCategoryDTO
from app.admin.services.AdmParameterCategoryService import AdmParameterCategoryService
from typing import List
from flask import jsonify
import json

class AdmParameterService:
    parameterCategoryService = AdmParameterCategoryService()

    def __init__(self):
        pass

    def findAll(self):
        plist = AdmParameter.query.all()
        return self.setTransientList(plist)

    def findById(self, id: int):
        obj = AdmParameter.query.filter(AdmParameter.id == id).first()
        return self.setTransient(obj)

    def save(self, form: AdmParameterForm):
        try:
            admParameter = form.to_AdmParameter()
            db.session.add(admParameter)
            db.session.commit()
            return self.setTransient(admParameter)
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def update(self, id: int, form: AdmParameterForm):
        try:
            admParameter: AdmParameter = AdmParameter.query.get(id)
            if admParameter != None:
                admParameter = form.from_AdmParameter(admParameter)
                db.session.commit()
                return self.setTransient(admParameter)
            else:
                return None
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def delete(self, id: int):
        try:
            query = AdmParameter.query.filter_by(id=id)
            if query.count() > 0:
                AdmParameter.query.filter(AdmParameter.id == id).delete()
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def setTransientList(self, plist: List[AdmParameter]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return jsonify(listaDTO)

    def setTransient(self, item: AdmParameter):
        dto = AdmParameterDTO(item)
        parameterCategory = self.parameterCategoryService.findById(item.idParameterCategory)
        dto.admParameterCategory = AdmParameterCategoryDTO(parameterCategory).__dict__
        
        return dto.__dict__