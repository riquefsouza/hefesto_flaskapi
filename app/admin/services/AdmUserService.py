from app import db
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserDTO import AdmUserDTO
from app.admin.schemas.AdmUserForm import AdmUserForm

class AdmUserService:
    def __init__(self):
        pass

    def findAll(self):
        return AdmUser.query.all()

    def findById(self, id: int):
        return AdmUser.query.filter(AdmUser.id == id).first()

    def save(self, form: AdmUserForm):
        try:
            admUser = form.to_AdmUser()
            db.session.add(admUser)
            db.session.commit()
            return admUser
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
                return admUser
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
