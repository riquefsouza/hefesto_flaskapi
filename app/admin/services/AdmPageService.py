from app import db
from app.admin.models.AdmPage import AdmPage
from app.admin.schemas.AdmPageForm import AdmPageForm
from app.admin.schemas.AdmPageDTO import AdmPageDTO
from app.admin.services.AdmPageProfileService import AdmPageProfileService
from typing import List
from flask import jsonify
import json

class AdmPageService:
    pageProfileService = AdmPageProfileService()

    def __init__(self):
        pass

    def findAll(self):
        plist = AdmPage.query.all()
        return self.setTransientList(plist)

    def findById(self, id: int):
        obj = AdmPage.query.filter(AdmPage.id == id).first()
        return self.setTransient(obj)

    def save(self, form: AdmPageForm):
        try:
            admPage = form.to_AdmPage()
            db.session.add(admPage)
            db.session.commit()
            return self.setTransient(admPage)
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def update(self, id: int, form: AdmPageForm):
        try:
            admPage: AdmPage = AdmPage.query.get(id)
            if admPage != None:
                admPage = form.from_AdmPage(admPage)
                db.session.commit()
                return self.setTransient(admPage)
            else:
                return None
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def delete(self, id: int):
        try:
            query = AdmPage.query.filter_by(id=id)
            if query.count() > 0:
                AdmPage.query.filter(AdmPage.id == id).delete()
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def setTransientList(self, plist: List[AdmPage]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return jsonify(listaDTO)

    def setTransient(self, item: AdmPage):
        dto = AdmPageDTO(item)
        obj = self.pageProfileService.getProfilesByPage(item.id)
        for profile in obj:
            dto.admIdProfiles.append(profile.id)

        listPageProfiles = []
        for profile in obj:
            listPageProfiles.append(profile.description)
        dto.pageProfiles = ",".join(listPageProfiles)
        
        return dto.__dict__