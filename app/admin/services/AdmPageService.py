from app import db
from app.admin.models.AdmPage import AdmPage
from app.admin.schemas.AdmPageForm import AdmPageForm

class AdmPageService:
    def __init__(self):
        pass

    def findAll(self):
        return AdmPage.query.all()

    def findById(self, id: int):
        return AdmPage.query.filter(AdmPage.id == id).first()

    def save(self, form: AdmPageForm):
        try:
            admPage = form.to_AdmPage()
            db.session.add(admPage)
            db.session.commit()
            return admPage
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
                return admPage
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
