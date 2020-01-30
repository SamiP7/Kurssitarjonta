from application import db

class User(db.Model):

	__tablename__ = "account"
  
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	email = db.Column(db.String(144), nullable=False)
	phonenumber = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)

	def __init__(self, name, email, phonenumber, password):
		self.name = name
		self.email = email
		self.phonenumber = phonenumber
		self.password = password
  
	def get_id(self):
		return self.id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True