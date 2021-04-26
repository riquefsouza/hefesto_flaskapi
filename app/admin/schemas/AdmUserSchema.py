from app import ma

class AdmUserSchema(ma.Schema):
	class Meta:
		fields = ('id','active','email','login','name','password')

adm_user_schema = AdmUserSchema()
adm_users_schema = AdmUserSchema(many=True)
