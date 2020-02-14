from flask_wtf import FlaskForm
from application.topics.models import Topic
from wtforms import StringField, DateField, SelectField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField


def all_topics():
	return Topic.query.all()
	
	
class CourseForm(FlaskForm):
	name = StringField("Course name", [validators.Length(min=5)])
	datestart = DateField("Course start", [validators.DataRequired("Start date is required")], format="%Y-%m-%d")
	dateend = DateField("Course end", [validators.DataRequired("End date is required")], format="%Y-%m-%d")
	place = StringField("Location", [validators.Length(min=5)])
	teachers = StringField("Teachers", [validators.Length(min=5)])
	desc = StringField("Description")
	topic = QuerySelectField(query_factory=all_topics, get_label='name', allow_blank=False)
	
	class Meta:
		csrf = False