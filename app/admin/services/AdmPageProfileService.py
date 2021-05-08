from app import db
from typing import List
from app.admin.models.AdmPage import AdmPage
from app.admin.models.AdmProfile import AdmProfile
from app.admin.models.AdmPageProfile import AdmPageProfile

class AdmPageProfileService:
    def __init__(self):
        pass

    def setTransient(self, list: List[AdmPageProfile]):
        for item in list:
            setTransient(item)
    
    def setTransient(self, item: AdmPageProfile):
        item.AdmPage = AdmPage.query.filter(AdmPage.id == item.idPage).first()
        item.AdmProfile = AdmProfile.query.filter(AdmProfile.id == item.idProfile).first()