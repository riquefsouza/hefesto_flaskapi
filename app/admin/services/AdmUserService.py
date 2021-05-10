from app import db
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserDTO import AdmUserDTO
from app.admin.schemas.AdmUserForm import AdmUserForm
from app.admin.services.AdmUserProfileService import AdmUserProfileService
from typing import List
from flask import jsonify
import json
#import bcrypt
from passlib.context import CryptContext

class AdmUserService:
    userProfileService = AdmUserProfileService()
    bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def __init__(self):
        pass

    def findAll(self):
        plist = AdmUser.query.all()
        return self.setTransientList(plist)

    def findById(self, id: int):
        obj = AdmUser.query.filter(AdmUser.id == id).first()
        return self.setTransient(obj)

    def save(self, form: AdmUserForm):
        try:
            admUser = form.to_AdmUser()
            db.session.add(admUser)
            db.session.commit()
            return self.setTransient(admUser)
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def update(self, id: int, form: AdmUserForm):
        try:
            admUser: AdmUser = AdmUser.query.get(id)
            if admUser != None:
                admUser = form.from_AdmUser(admUser)
                db.session.commit()
                return self.setTransient(admUser)
            else:
                return None
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def delete(self, id: int):
        try:
            query = AdmUser.query.filter_by(id=id)
            if query.count() > 0:
                AdmUser.query.filter(AdmUser.id == id).delete()
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def setTransientList(self, plist: List[AdmUser]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return jsonify(listaDTO)

    def setTransient(self, item: AdmUser):
        dto = AdmUserDTO(item)
        obj = self.userProfileService.getProfilesByUser(item.id)
        for profile in obj:
            dto.admIdProfiles.append(profile.id)

        listUserProfiles = []
        for profile in obj:
            listUserProfiles.append(profile.description)
        dto.userProfiles = ",".join(listUserProfiles)
        
        return dto.__dict__            

    def authenticate(self, login: str, password: str):
        admUser = AdmUser.query.filter(AdmUser.login == login).first()

        if admUser != None:
            if self.verifyPassword(password, admUser.password):
                return admUser

        return None

    def verifyPassword(self, password: str, hashPassword: str):
        #return bcrypt.checkpw(password, hashPassword)
        return self.bcrypt.verify(password, hashPassword)

    def register(self, model: AdmUser):
        #hash = bcrypt.hashpw(model.password.encode('utf8'), bcrypt.gensalt(10))
        hash = self.bcrypt.hash(model.password.encode('utf8'))
        model.password = hash
