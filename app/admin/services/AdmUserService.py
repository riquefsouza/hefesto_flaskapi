from app import db
from app.admin.models.AdmUser import AdmUser
from app.admin.schemas.AdmUserDTO import AdmUserDTO
from app.admin.schemas.AdmUserForm import AdmUserForm
#import bcrypt
from passlib.context import CryptContext

class AdmUserService:
    bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
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
