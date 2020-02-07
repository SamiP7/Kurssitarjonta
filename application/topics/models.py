from application import db
from application.courses.models import Course

from sqlalchemy.sql import text

class Topic(db.Model):

	__tablename__ = "topic"
	
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(144), nullable=False)

	def __init__(self, name):
		self.name = name
		
	def get_id(self):
		return self.id
		
	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True
		
	@staticmethod
	def find_courses_by_topic():	
		stmt = text("SELECT * FROM Course"
					" LEFT JOIN Topic ON Topic.id = Course.topic_id")
		res = db.engine.execute(stmt)
		
		response = []
		for row in res:
			response.append({"topic_id":row[9], "name":row[1]})
			
		return response
	
	@staticmethod
	def all_topics():
		stmt = text("SELECT DISTINCT * FROM Topic")
		res = db.engine.execute(stmt)
		
		response = []
		for row in res:
			response.append({"id":row[0], "name":row[1]})
			
		return response