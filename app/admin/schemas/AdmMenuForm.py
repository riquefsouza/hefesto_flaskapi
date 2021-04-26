from app.admin.models.AdmMenu import AdmMenu
from typing import Dict


class AdmMenuForm:
    description: str
    idMenuParent: int
    idPage: int
    order: int
    #admMenuParent
    #admPage
    
    def __init__(self, admMenu: Dict):
        self.description=admMenu["description"]
        self.idMenuParent=admMenu["idMenuParent"]
        self.idPage=admMenu["idPage"]
        self.order=admMenu["order"]

    def to_AdmMenu(self):
        newAdmMenu = AdmMenu(
            description=self.description,
            idMenuParent=self.idMenuParent,
            idPage=self.idPage,
            order=self.order
        )
        return newAdmMenu

    def from_AdmMenu(self, admMenu: AdmMenu):
        admMenu.description=self.description
        admMenu.idMenuParent=self.idMenuParent
        admMenu.idPage=self.idPage
        admMenu.order=self.order

        return admMenu
