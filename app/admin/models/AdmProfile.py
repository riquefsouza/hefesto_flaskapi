from app import db


class AdmProfile(db.Model):
    __tablename__ = 'adm_profile'

    id = db.Column('prf_seq', db.BigInteger, db.Sequence('adm_profile_seq'), primary_key=True)
    administrator = db.Column('prf_administrator', db.CHAR(1), nullable=False, default='N')
    description = db.Column('prf_description', db.String(255), nullable=False, unique=True)
    general = db.Column('prf_general', db.CHAR(1), nullable=False, default='N')

    def __repr__(self):
        return '<AdmProfile %r>' % self.name
