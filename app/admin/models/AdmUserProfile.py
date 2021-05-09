from app import db


class AdmUserProfile(Base):
    __tablename__ = 'adm_user_profile'

    id = db.Column('usp_seq', db.BigInteger, db.Sequence('adm_user_profile_seq'), primary_key=True)
    idProfile = db.Column('usp_prf_seq', db.BigInteger, db.ForeignKey('adm_profile.prf_seq'), nullable=False)
    idUser = db.Column('usp_use_seq', db.BigInteger, db.ForeignKey('adm_user.usu_seq'), nullable=False)
    admProfile = db.relationship('AdmProfile', foreign_keys=idProfile)
    admUser = db.relationship('AdmUser', foreign_keys=idUser)

    #def __repr__(self):
    #    return '<AdmUserProfile %r>' % self.description
