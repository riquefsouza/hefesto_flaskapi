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
            newAdmUser = form.to_AdmUser()
            db.session.add(newAdmUser)
            db.session.commit()
            return newAdmUser
        except Exception as e:
            print(e)
            db.session.rollback()
            return Null

    def update(self, id: int, form: AdmUserForm):
        try:
            admUser: AdmUser = AdmUser.query.get(id)
            admUser = form.from_AdmUser(admUser)
            db.session.commit()
            return admUser
        except Exception as e:
            print(e)
            db.session.rollback()
            return Null

    def delete(self, id: int):
        try:
            AdmUser.query.filter(AdmUser.id == id).delete()
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
