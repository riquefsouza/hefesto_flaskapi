from app import ma
from marshmallow import fields

class AdmPageSchema(ma.Schema):
	admIdProfiles = fields.List(fields.Int())
	pageProfiles = fields.Str()
	class Meta:
		fields = ('id', 'description', 'url')

admPage_schema = AdmPageSchema()
admPage_schemaMany = AdmPageSchema(many=True)
