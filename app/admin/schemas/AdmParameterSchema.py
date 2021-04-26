from app import ma


class AdmParameterSchema(ma.Schema):
	class Meta:
		fields = ('id','code','description','idParameterCategory','value')
    #admParameterCategory

admParameter_schema = AdmParameterSchema()
admParameter_schemaMany = AdmParameterSchema(many=True)
