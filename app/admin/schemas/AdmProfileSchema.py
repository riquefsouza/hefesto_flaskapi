from app import ma


class AdmProfileSchema(ma.Schema):
	class Meta:
		fields = ('id','administrator','description','general','admPages','admUsers','profilePages','profileUsers')

admProfile_schema = AdmProfileSchema()
admProfile_schemaMany = AdmProfileSchema(many=True)
