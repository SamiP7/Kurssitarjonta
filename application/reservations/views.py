from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.reservations.models import Reservation
from application.auth.models import User
from application.courses.models import Course
from application.reservations.forms import ReservationForm
from application.courses.models import Course

@app.route("/reservations", methods=["GET"])
@login_required(role="ANY")
def reservations_index():
	return render_template("reservations/list.html", reservations = Reservation.my_reservations(current_user.id))

@app.route("/reservations/<course_id>/join/", methods=["GET"])
@login_required(role="ANY")
def reservations_form(course_id):
	return render_template("reservations/new.html", form=ReservationForm(), course=Course.query.get(course_id))
	
	
@app.route("/reservations/<course_id>/join", methods=["POST"])
@login_required(role="ANY")	
def create_reservation(course_id):
	form = ReservationForm(request.form)
	
	if not form.validate():
		return render_template("reservations/new.html", form=form, course=Course.query.get(course_id))
	if (Reservation.query.filter_by(course_id=course_id).filter_by(account_id=current_user.id).first() is None
	and Course.query.filter_by(id=course_id).filter(Course.users.any(id=current_user.id)).first() is None):
		r = Reservation(form.accountnumber.data, form.indexnumber.data, form.amount.data)
		r.haspaid = False
		r.account_id = current_user.id
		r.course_id = course_id
	
		db.session().add(r)
		db.session().commit()
	
	return redirect(url_for("reservations_index"))
	
@app.route("/reservations/<reservation_id>/delete", methods=["POST"])
@login_required(role="ANY")
def delete_reservation(reservation_id):
	Reservation.query.filter_by(id=reservation_id).delete()
	
	db.session().commit()
	return redirect(url_for("reservations_index"))
	
@app.route("/reservations/<reservation_id>/", methods=["POST"])
@login_required(role="ANY")
def reservation_paid(reservation_id):

	r = Reservation.query.get(reservation_id)
	if not r.haspaid:
		r.haspaid = True

		course = Course.query.filter_by(id=r.course_id).first()
		account = current_user
		course.users.append(account)
		db.session().add(course)
		db.session().commit()
	
	return redirect(url_for("reservations_index"))
