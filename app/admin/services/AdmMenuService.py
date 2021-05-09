from app import db
from app.admin.models.AdmMenu import AdmMenu
from app.admin.schemas.AdmMenuForm import AdmMenuForm
from typing import List


class AdmMenuService:
    def __init__(self):
        pass

    def findAll(self):
        return AdmMenu.query.all()

    def findById(self, id: int):
        return AdmMenu.query.filter(AdmMenu.id == id).first()

    def save(self, form: AdmMenuForm):
        try:
            admMenu = form.to_AdmMenu()
            db.session.add(admMenu)
            db.session.commit()
            return admMenu
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def update(self, id: int, form: AdmMenuForm):
        try:
            admMenu: AdmMenu = AdmMenu.query.get(id)
            if admMenu != None:
                admMenu = form.from_AdmMenu(admMenu)
                db.session.commit()
                return admMenu
            else:
                return None
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    def delete(self, id: int):
        try:
            query = AdmMenu.query.filter_by(id=id)
            if query.count() > 0:
                AdmMenu.query.filter(AdmMenu.id == id).delete()
                db.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def setTransientWithoutSubMenus(self, list: List[AdmMenu]):
        for item in list:
            self.setTransientSubMenus(item, None);

    def setTransient(self, list: List[AdmMenu]):
        for item in list:
            self.setTransient(item)

    def setTransientSubMenus(self, item: AdmMenu, subMenus: List[AdmMenu]):
        if item.admPage != None:
            item.url = item.admPage.url
        else:
            item.url = None
        item.subMenus = subMenus
    
    def setTransient(self, item: AdmMenu):
        self.setTransientSubMenus(item, self.findByIdMenuParent(item.id))

    def findByIdMenuParent(self, idMenuParent: int):
        if idMenuParent != None:
            lista = AdmMenu.query.filter(AdmMenu.idMenuParent == idMenuParent)
            #self.setTransientWithoutSubMenus(lista)
            return lista
        
        return []
    
    def mountMenuItem(self, listIdProfile: List[int]):
        pass

