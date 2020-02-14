from application import db
from wtforms.validators import ValidationError

class User(db.Model):

	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	email = db.Column(db.String(144), nullable=False)
	phonenumber = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)
	urole = db.Column(db.String(80))

	def __init__(self, name, email, phonenumber, password, urole):
		self.name = name
		self.email = email
		self.phonenumber = phonenumber
		self.password = password
		self.urole = urole
  
	def get_id(self):
		return self.id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True
	
	def get_urole(self):
		return self.urole
	
class Unique(object):
	def __init__(self, model, field, message=None):
		self.model = model
		self.field = field
		message = "This email is already in use"
		self.message = message

	def __call__(self, form, field):         
		check = self.model.query.filter(self.field == field.data).first()
		if check:
			raise ValidationError(self.message)