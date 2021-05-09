from app import db


class AdmPageProfile(db.Model):
    __tablename__ = 'adm_page_profile'

    id = db.Column('pgl_seq', db.BigInteger, db.Sequence('adm_page_profile_seq'), primary_key=True)
    idProfile = db.Column('pgl_prf_seq', db.BigInteger, db.ForeignKey('adm_profile.prf_seq'), nullable=False)
    idPage = db.Column('pgl_pag_seq', db.BigInteger, db.ForeignKey('adm_page.pag_seq'), nullable=False)
    admProfile = db.relationship('AdmProfile', foreign_keys=idProfile)
    admPage = db.relationship('AdmPage', foreign_keys=idPage)

    #def __repr__(self):
    #    return '<AdmPageProfile %r>' % self.description
