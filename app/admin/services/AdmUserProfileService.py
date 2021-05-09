from app import db
from typing import List
from app.admin.models.AdmUser import AdmUser
from app.admin.models.AdmProfile import AdmProfile
from app.admin.models.AdmUserProfile import AdmUserProfile

class AdmUserProfileService:
    def __init__(self):
        pass

    #def setTransient(self, list: List[AdmUserProfile]):
    #    for item in list:
    #        setTransient(item)
    
    #def setTransient(self, item: AdmUserProfile):
    #    item.AdmUser = AdmUser.query.filter(AdmUser.id == item.idUser).first()
    #    item.AdmProfile = AdmProfile.query.filter(AdmProfile.id == item.idProfile).first()

    def findAll(self):
        listAdmUserProfile = AdmUser.query.all()
        #self.setTransient(listAdmUserProfile)
        return listAdmUserProfile
        
    def getProfilesByUser(self, admUserId: int):
        listAdmUserProfile = AdmUserProfile.query.filter(AdmUserProfile.idUser == admUserId)
        lista: List[AdmProfile]

        for item in lista:
            #self.setTransient(item)
            lista.append(item.admProfile)

        return lista

    def getUsersByProfile(self, admProfileId: int):
        listAdmUserProfile = AdmUserProfile.query.filter(AdmUserProfile.idProfile == admProfileId)
        lista: List[AdmUser]

        for item in lista:
            #self.setTransient(item)
            lista.append(item.admUser)

        return lista

