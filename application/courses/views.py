from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db, login_required
from application.courses.models import Course
from application.auth.models import User
from application.reservations.models import Reservation
from application.topics import models
from application.auth import models
from application.courses.forms import CourseForm
from application.reservations import views
from application.reservations.forms import ReservationForm

@app.route("/courses/search_students/", methods=["GET", "POST"])
@login_required(role="ADMIN")
def search_students_options():
	return render_template("courses/user_in_course.html", all_courses=Course.all_courses())

@app.route("/courses/search", methods=["GET", "POST"])
@login_required(role="ADMIN")
def search_students():
	name = request.form.get("option")
	return render_template("auth/user_in_course.html", students_in_course=Course.find_student_by_course(name))
	
@app.route("/courses/search/delete/<course_id>/<account_id>", methods=["GET", "POST"])
@login_required(role="ADMIN")
def delete_attendance_admin(course_id, account_id):
	Reservation.query.filter_by(course_id=course_id).filter_by(account_id=account_id).delete()
	course = Course.query.filter_by(id=course_id).first()
	
	tbd = db.session.query(User).filter_by(id=account_id).first()
	course.users.remove(tbd)
	db.session().commit()
	
	return render_template("courses/user_in_course.html", all_courses=Course.all_courses())
@app.route("/courses/user_course/")
@login_required(role="ANY")
def my_courses():
	return render_template("courses/user_courses.html", my_courses=Course.find_my_courses(current_user.id))
	
@app.route("/courses/user_course/<course_id>", methods=["POST"])
@login_required(role="ANY")
def delete_attendance(course_id):
	Reservation.query.filter_by(course_id=course_id).filter_by(account_id=current_user.id).delete()
	
	course = Course.query.filter_by(id=course_id).first()
	tbd = db.session.query(User).filter_by(id=current_user.id).first()
	course.users.remove(tbd)
	db.session().commit()
	return render_template("courses/user_courses.html", my_courses=Course.find_my_courses(current_user.id))

@app.route("/courses/<course_id>/info", methods=["POST"])
def course_info(course_id):
	return render_template("courses/info.html", courses = Course.query.filter_by(id=course_id))

@app.route("/courses", methods=["GET"])
def courses_index():
	return render_template("courses/list.html", courses = Course.query.all())

@app.route("/courses/<course_id>/", methods=["POST"])
@login_required(role="ADMIN")
def delete_course(course_id):
	if (Reservation.query.filter_by(course_id=course_id).first() is None and
		Course.query.filter_by(id=course_id).filter(Course.users.any()).first() is None):
		Course.query.filter_by(id=course_id).delete()
		db.session().commit()
	
	return redirect(url_for("courses_index"))

@app.route("/courses/new")
@login_required(role="ADMIN")
def courses_form():
	return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/", methods=["POST"])
@login_required(role="ADMIN")
def courses_create():
	form = CourseForm(request.form)
	
	if not form.validate():
		return render_template("courses/new.html", form = form)
	
	course = Course(form.name.data, form.datestart.data, form.dateend.data, form.place.data, 
					form.teachers.data, form.desc.data, form.topic.data)
					
	db.session().add(course)
	db.session().commit()
	
	return redirect(url_for("courses_index"))