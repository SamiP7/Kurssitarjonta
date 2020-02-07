from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.courses.models import Course
from application.topics.models import Topic
from application.courses.forms import CourseForm

@app.route("/courses", methods=["GET"])
def courses_index():
	return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/<course_id>/", methods=["POST"])
@login_required
def delete_course(course_id):

	Course.query.filter_by(id=course_id).delete()
	db.session().commit()
	
	return redirect(url_for("courses_index"))

@app.route("/courses/new")
@login_required
def courses_form():
	return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/", methods=["POST"])
@login_required
def courses_create():
	form = CourseForm(request.form)
	
	if not form.validate():
		return render_template("courses/new.html", form = form)
	
	course = Course(form.name.data, form.datestart.data, form.dateend.data, form.place.data, 
					form.teachers.data, form.desc.data, form.topic.data)
					
	db.session().add(course)
	db.session().commit()
	
	return redirect(url_for("courses_index"))