from application import db

from sqlalchemy.sql import text

class Reservation(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	accountnumber = db.Column(db.String(144), nullable=False)
	indexnumber = db.Column(db.Integer, nullable=False)
	amount = db.Column(db.Integer, nullable=False)
	haspaid = db.Column(db.Boolean, nullable=False)
	
	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
	course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

	def __init__(self, accountnumber, indexnumber, amount):
		self.accountnumber = accountnumber
		self.indexnumber = indexnumber
		self.amount = amount
		self.haspaid = False
	
	def get_id(self):
		return self.id
  
	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True
	
	@staticmethod
	def my_reservations(id):
		stmt = text("SELECT * FROM Reservation"
				" LEFT JOIN Course ON Course.id = Reservation.course_id"
				" LEFT JOIN Account ON Account.id = Reservation.account_id"
				" WHERE Account.id = :id").params(id=id)
		res = db.engine.execute(stmt)
		
		response = []
		for row in res:
			response.append({"id":row[0], "accountnumber":row[1], "indexnumber":row[2], "amount":row[3], "haspaid":row[4], "cid":row[7],
			 "cname":row[8], "cstart":row[9], "cend":row[10], "cplace":row[11], "cteachers":row[12], "cdesc":row[13]})
		
		return response