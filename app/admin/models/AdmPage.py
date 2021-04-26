from app import db

class AdmPage(db.Model):
    __tablename__ = 'adm_page'

    id = db.Column('pag_seq', db.BigInteger, db.Sequence('adm_page_seq'), primary_key=True)
    description = db.Column('pag_description', db.String(255), nullable=False, unique=True)
    url = db.Column('pag_url', db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return '<AdmPage %r>' % self.description
