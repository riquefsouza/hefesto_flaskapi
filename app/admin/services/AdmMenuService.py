from app import db
from app.admin.models.AdmMenu import AdmMenu
from app.admin.schemas.AdmMenuForm import AdmMenuForm
from app.admin.schemas.AdmMenuDTO import AdmMenuDTO
from typing import List
from flask import jsonify
import json

class AdmMenuService:
    def __init__(self):
        pass

    def findAll(self):
        plist = AdmMenu.query.all()
        return self.setTransientList(plist)

    def findById(self, id: int):
        obj = AdmMenu.query.filter(AdmMenu.id == id).first()
        return self.setTransient(obj)

    def save(self, form: AdmMenuForm):
        try:
            admMenu = form.to_AdmMenu()
            db.session.add(admMenu)
            db.session.commit()
            return self.setTransient(admMenu)
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
                return self.setTransient(admMenu)
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

    def setTransientWithoutSubMenus(self, plist: List[AdmMenuDTO]):
        listaDTO = []
        for item in plist:
            dto = self.setTransientSubMenus(item, None)
            listaDTO.append(dto)
        return jsonify(listaDTO)

    def setTransientList(self, plist: List[AdmMenu]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return jsonify(listaDTO)

    def setTransientSubMenus(self, item: AdmMenu, subMenus: List[AdmMenuDTO]):
        dto = AdmMenuDTO(item)
        if item.admPage != None:
            dto.url = item.admPage.url
        else:
            dto.url = None
        dto.subMenus = subMenus

        return dto.__dict__
    
    def setTransient(self, item: AdmMenu):
        listaMenus = self.findByIdMenuParent(item.id)
        listaDTO = []
        for menu in listaMenus:
            menuDTO = AdmMenuDTO(menu)
            listaDTO.append(menuDTO.__dict__)

        return self.setTransientSubMenus(item, listaDTO)

    def findByIdMenuParent(self, idMenuParent: int):
        if idMenuParent != None:
            lista = AdmMenu.query.filter_by(idMenuParent = idMenuParent).all()
            #self.setTransientWithoutSubMenus(lista)
            return lista
        
        return []
    
    def findMenuByIdProfiles(self, listaIdProfile: List[int], admMenu: AdmMenu):
        pass

    def findAdminMenuByIdProfiles(self, listaIdProfile: List[int], admMenu: AdmMenu):
        pass

    def findMenuParentByIdProfiles(self, listaIdProfile: List[int]):
        pass
    
    def findAdminMenuParentByIdProfiles(self, listaIdProfile: List[int]):
        pass

    def mountMenuItem(self, listIdProfile: List[int]):
        pass

