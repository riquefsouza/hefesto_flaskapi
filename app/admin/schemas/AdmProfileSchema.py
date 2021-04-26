from app import ma


class AdmProfileSchema(ma.Schema):
	class Meta:
		fields = ('id','administrator','description','general')

admProfile_schema = AdmProfileSchema()
admProfile_schemaMany = AdmProfileSchema(many=True)
