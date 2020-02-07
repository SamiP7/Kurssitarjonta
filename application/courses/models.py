from application import db

class Course(db.Model):

	__tablename__ = "course"
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(144), nullable=False)
	date_start = db.Column(db.Date)
	date_end = db.Column(db.Date)
	place = db.Column(db.String(144), nullable=False)
	teachers = db.Column(db.String(144), nullable=False)
	desc = db.Column(db.String(1440), nullable=False)
	
	topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
	topic = db.relationship('Topic', backref=db.backref('courses', lazy='dynamic'))
	
	def __init__(self, name, date_start, date_end, place, teachers, desc, topic):
		self.name = name
		self.date_start = date_start
		self.date_end = date_end
		self.place = place
		self.teachers = teachers
		self.desc = desc
		self.topic = topic
		
	def get_id(self):
		return self.id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True