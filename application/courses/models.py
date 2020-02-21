from application import db
from application.auth.models import User

from sqlalchemy.sql import text

coursestudent = db.Table("coursestudent",
		db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True),
		db.Column("account_id", db.Integer, db.ForeignKey("account.id"), primary_key=True)
	)

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
	
	users = db.relationship("User", secondary=coursestudent, backref="courses")
	reservations = db.relationship("Reservation", backref='course', lazy=True)
	
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
		
		
		
	@staticmethod
	def find_my_courses(id):
		stmt = text("SELECT * FROM Course"
				" LEFT JOIN CourseStudent ON CourseStudent.course_id = Course.id"
				" LEFT JOIN Account ON Account.id = CourseStudent.account_id"
				" WHERE Account.id = :id").params(id=id)
		res = db.engine.execute(stmt)

		response = []
		for row in res:
			response.append({"id":row[0], "name":row[1], "start":row[2], "end":row[3], "place":row[4], "teachers":row[5], "desc":row[6]})
			
		return response
		
	@staticmethod
	def all_courses():
		stmt = text("SELECT DISTINCT * FROM Course")
		res = db.engine.execute(stmt)
		
		response = []
		for row in res:
			response.append({"id":row[0], "name":row[1]})
			
		return response
		
	@staticmethod
	def find_student_by_course(id):
		stmt = text("SELECT * FROM Course"
				" JOIN CourseStudent ON CourseStudent.course_id = Course.id"
				" JOIN Account ON Account.id = CourseStudent.account_id"
				" WHERE Course.id = :id").params(id=id)
				
		res = db.engine.execute(stmt)
		response = []
		
		for row in res:
			response.append({"cid":row[0], "sid":row[9], "name":row[11], "email":row[12], "role":row[15]})

		return response