from app import db
from app.admin.models.AdmProfile import AdmProfile
from app.admin.schemas.AdmProfileForm import AdmProfileForm
from app.admin.schemas.AdmProfileDTO import AdmProfileDTO
from app.admin.schemas.AdmPageDTO import AdmPageDTO
from app.admin.schemas.AdmUserDTO import AdmUserDTO
from app.admin.services.AdmPageProfileService import AdmPageProfileService
from app.admin.services.AdmUserProfileService import AdmUserProfileService
from typing import List
from flask import jsonify
import json

class AdmProfileService:
    pageProfileService = AdmPageProfileService()
    userProfileService = AdmUserProfileService()

    def __init__(self):
        pass

    def findAll(self):
        plist = AdmProfile.query.all()
        return self.setTransientList(plist)

    def findById(self, id: int):
        obj = AdmProfile.query.filter(AdmProfile.id == id).first()
        return self.setTransient(obj)

    def save(self, form: AdmProfileForm):
        try:
            admProfile = form.to_AdmProfile()
            db.session.add(admProfile)
            db.session.commit()
            return self.setTransient(admProfile)
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def update(self, id: int, form: AdmProfileForm):
        try:
            admProfile: AdmProfile = AdmProfile.query.get(id)
            if admProfile != None:
                admProfile = form.from_AdmProfile(admProfile)
                db.session.commit()
                return self.setTransient(admProfile)
            else:
                return None
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def delete(self, id: int):
        try:
            query = AdmProfile.query.filter_by(id=id)
            if query.count() > 0:
                AdmProfile.query.filter(AdmProfile.id == id).delete()
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def setTransientList(self, plist: List[AdmProfile]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return jsonify(listaDTO)

    def setTransient(self, item: AdmProfile):
        dto = AdmProfileDTO(item)
        obj = self.pageProfileService.getPagesByProfile(item.id)
        for page in obj:
            pageDTO = AdmPageDTO(page)
            dto.admPages.append(pageDTO.__dict__)

        listProfilePages = []
        for page in obj:
            listProfilePages.append(page.description)
        dto.profilePages = ",".join(listProfilePages)

        obj = self.userProfileService.getUsersByProfile(item.id)
        for user in obj:
            userDTO = AdmUserDTO(user)
            dto.admUsers.append(userDTO.__dict__)

        listProfileUsers = []
        for user in obj:
            listProfileUsers.append(user.name)
        dto.profileUsers = ",".join(listProfileUsers)

        return dto.__dict__

    def findProfilesByPage(self, pageId: int):
        return self.pageProfileService.getProfilesByPage(pageId)

    def findProfilesByUser(self, userId: int):
        return self.userProfileService.getProfilesByUser(userId)
