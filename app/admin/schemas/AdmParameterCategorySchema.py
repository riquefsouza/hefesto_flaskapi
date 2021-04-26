from app import ma

class AdmParameterCategorySchema(ma.Schema):
	class Meta:
		fields = ('id','description', 'order')

admParameterCategory_schema = AdmParameterCategorySchema()
admParameterCategory_schemaMany = AdmParameterCategorySchema(many=True)
