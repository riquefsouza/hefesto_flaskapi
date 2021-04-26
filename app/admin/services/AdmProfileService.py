from app import db
from app.admin.models.AdmProfile import AdmProfile
from app.admin.schemas.AdmProfileForm import AdmProfileForm

class AdmProfileService:
    def __init__(self):
        pass

    def findAll(self):
        return AdmProfile.query.all()

    def findById(self, id: int):
        return AdmProfile.query.filter(AdmProfile.id == id).first()

    def save(self, form: AdmProfileForm):
        try:
            admProfile = form.to_AdmProfile()
            db.session.add(admProfile)
            db.session.commit()
            return admProfile
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
                return admProfile
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
