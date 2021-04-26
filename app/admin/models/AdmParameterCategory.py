from app import db

class AdmParameterCategory(db.Model):
    __tablename__ = 'adm_parameter_category'

    id = db.Column('pmc_seq', db.BigInteger, db.Sequence('adm_parameter_category_seq'), primary_key=True)
    description = db.Column('pmc_description', db.String(64), nullable=False, unique=True)
    order = db.Column('pmc_order', db.BigInteger)

    def __repr__(self):
        return '<AdmParameterCategory %r>' % self.description
