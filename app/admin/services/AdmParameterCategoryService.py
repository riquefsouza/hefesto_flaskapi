from app import db
from app.admin.models.AdmParameterCategory import AdmParameterCategory
from app.admin.schemas.AdmParameterCategoryForm import AdmParameterCategoryForm

class AdmParameterCategoryService:
    def __init__(self):
        pass

    def findAll(self):
        return AdmParameterCategory.query.all()

    def findById(self, id: int):
        return AdmParameterCategory.query.filter(AdmParameterCategory.id == id).first()

    def save(self, form: AdmParameterCategoryForm):
        try:
            admParameterCategory = form.to_AdmParameterCategory()
            db.session.add(admParameterCategory)
            db.session.commit()
            return admParameterCategory
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def update(self, id: int, form: AdmParameterCategoryForm):
        try:
            admParameterCategory: AdmParameterCategory = AdmParameterCategory.query.get(id)
            if admParameterCategory != None:
                admParameterCategory = form.from_AdmParameterCategory(admParameterCategory)
                db.session.commit()
                return admParameterCategory
            else:
                return None
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def delete(self, id: int):
        try:
            query = AdmParameterCategory.query.filter_by(id=id)
            if query.count() > 0:
                AdmParameterCategory.query.filter(AdmParameterCategory.id == id).delete()
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
