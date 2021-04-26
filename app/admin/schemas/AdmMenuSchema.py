from app import ma

class AdmMenuSchema(ma.Schema):
	class Meta:
		fields = ('id','description','idMenuParent','idPage','order')
        #'admMenuParent', 'admPage', 

admMenu_schema = AdmMenuSchema()
admMenu_schemaMany = AdmMenuSchema(many=True)
