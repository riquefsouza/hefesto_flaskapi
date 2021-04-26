from app import db
from app.admin.models.AdmParameter import AdmParameter
from app.admin.schemas.AdmParameterForm import AdmParameterForm

class AdmParameterService:
    def __init__(self):
        pass

    def findAll(self):
        return AdmParameter.query.all()

    def findById(self, id: int):
        return AdmParameter.query.filter(AdmParameter.id == id).first()

    def save(self, form: AdmParameterForm):
        try:
            admParameter = form.to_AdmParameter()
            db.session.add(admParameter)
            db.session.commit()
            return admParameter
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
                return admParameter
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
