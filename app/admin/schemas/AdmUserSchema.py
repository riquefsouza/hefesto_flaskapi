from app import ma

class AdmUserSchema(ma.Schema):
	class Meta:
		fields = ('id','active','email','login','name','password',
		'admIdProfiles','userProfiles','currentPassword','newPassword','confirmNewPassword')

admUser_schema = AdmUserSchema()
admUser_schemaMany = AdmUserSchema(many=True)
