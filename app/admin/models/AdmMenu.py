from app import db


class AdmMenu(db.Model):
    __tablename__ = 'adm_menu'

    id = db.Column('mnu_seq', db.BigInteger, db.Sequence('adm_menu_seq'), primary_key=True)
    description = db.Column('mnu_description', db.String(255), nullable=False, unique=True)
    idMenuParent = db.Column('mnu_parent_seq', db.BigInteger, db.ForeignKey('adm_menu.mnu_seq'))
    idPage = db.Column('mnu_pag_seq', db.BigInteger, db.ForeignKey('adm_page.pag_seq'))
    order = db.Column('mnu_order', db.Integer)
    admMenuParent = db.relationship('AdmMenu', foreign_keys=idMenuParent)
    admPage = db.relationship('AdmPage', foreign_keys=idPage)

    def __repr__(self):
        return '<AdmMenu %r>' % self.description
