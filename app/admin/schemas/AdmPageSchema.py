from app import ma

class AdmPageSchema(ma.Schema):
	class Meta:
		fields = ('id', 'description', 'url')

admPage_schema = AdmPageSchema()
admPage_schemaMany = AdmPageSchema(many=True)
