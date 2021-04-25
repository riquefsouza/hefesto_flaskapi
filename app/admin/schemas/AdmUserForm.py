from app.admin.models.AdmUser import AdmUser
from typing import Dict

class AdmUserForm:
    email: str
    login: str
    name: str
    password: str
    active: str
    
    def __init__(self, admUser: Dict):
        self.active = admUser["active"]
        self.email=admUser["email"]
        self.login=admUser["login"]
        self.name=admUser["name"]
        self.password=admUser["password"]

    def to_AdmUser(self):
        newAdmUser = AdmUser(
            active=self.active,
            email=self.email,
            login=self.login,
            name=self.name,
            password=self.password
        )
        return newAdmUser

    def from_AdmUser(self, admUser: AdmUser):
        admUser.active = self.active
        admUser.email=self.email
        admUser.login=self.login
        admUser.name=self.name
        admUser.password=self.password

        return admUser
        