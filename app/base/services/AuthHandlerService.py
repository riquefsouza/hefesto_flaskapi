import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.base.schemas.UserDTO import UserDTO
from app.base.schemas.TokenDTO import TokenDTO
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity

class AuthHandlerService():
	pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
	#secret = '2!c_*_b4jm719vm4-8w@q=pyf)kl05b#%t9ol@-pywu-gep$qi'
	
	def get_password_hash(self, password):
		return self.pwd_context.hash(password)
	
	def verify_password(self, plain_password, hashed_password):
		return self.pwd_context.verify(plain_password, hashed_password)
	
	def encode_token(self, user: UserDTO):
		#payload = {
		#	'exp': datetime.utcnow() + timedelta(days=0, minutes=30),
		#	'iat': datetime.utcnow(),
		#	'sub': user.name,
		#	'id': user.id,
		#	'name': user.name,
		#	'email': user.email
		#}
		#token = jwt.encode(payload, self.secret, algorithm='HS256')

		additional_claims = {
			'id': user.id,
			'name': user.name,
			'email': user.email
		}
		token = create_access_token(identity=user.name, additional_claims=additional_claims)

		dto = TokenDTO(token, "Bearer")
		return dto
		
	def decode_token(self, token):
		try:
			current_user = get_jwt_identity()
			#payload = jwt.decode(token, self.secret, algorithms=['HS256'])

			user = UserDTO()
			user.id = payload['id']
			user.name = payload['name']
			user.email = payload['email']

			return user
		except jwt.ExpiredSignatureError:
			raise HTTPException(status_code=401, detail='Signature has expired')
		except jwt.InvalidTokenError as e:
			raise HTTPException(status_code=401, detail='Invalid token')
			
	#def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
	#	return self.decode_token(auth.credentials)
		
