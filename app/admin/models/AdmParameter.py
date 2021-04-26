from app import db


class AdmParameter(db.Model):
    __tablename__ = 'adm_parameter'

    id = db.Column('par_seq', db.BigInteger, db.Sequence('adm_parameter_seq'), primary_key=True)
    code = db.Column('par_code', db.String(64), nullable=False)
    description = db.Column('par_description', db.String(255), nullable=False, unique=True)
    idParameterCategory = db.Column('par_pmc_seq', db.BigInteger, db.ForeignKey('adm_parameter_category.pmc_seq'), nullable=False)
    value = db.Column('par_value', db.String(4000))
    admParameterCategory = db.relationship('AdmParameterCategory', foreign_keys=idParameterCategory)

    def __repr__(self):
        return '<AdmParameter %r>' % self.description
