from app import db

class AdmUser(db.Model):
    __tablename__ = 'adm_user'

    id = db.Column('usu_seq', db.BigInteger, db.Sequence('adm_user_seq'), primary_key=True)
    active = db.Column('usu_active', db.CHAR, nullable=False, default='N')
    email = db.Column('usu_email', db.String(255), unique=True)
    login = db.Column('usu_login', db.String(64), nullable=False, unique=True)
    name = db.Column('usu_name', db.String(64), unique=True)
    password = db.Column('usu_password', db.String(128), nullable=False, unique=True)

    #def __init__(self, login):
    #    self.login = login
    
    def __repr__(self):
        return '<AdmUser %r>' % self.name
