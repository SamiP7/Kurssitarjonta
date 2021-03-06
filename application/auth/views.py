from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login/", methods = ["GET", "POST"])
def auth_login():
	if request.method == "GET":
		return render_template("auth/loginform.html", form = LoginForm())

	form = LoginForm(request.form)

	user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
	if not user:
		return render_template("auth/loginform.html", form = form,
							error = "No such email or password is incorrect")


	login_user(user)
	return redirect(url_for("index"))
	
	
@app.route("/auth/logout/")
def auth_logout():
	logout_user()
	return redirect(url_for("index"))

@app.route("/auth/new/")
def auth_form():
	return render_template("auth/new.html", form = LoginForm())
	
@app.route("/auth/", methods=["POST"])
def new_user():
	form = LoginForm(request.form)
	
	if not form.validate():
		return render_template("auth/new.html", form = form)
	
	user = User(form.name.data, form.email.data, form.phonenumber.data, form.password.data, "ANY")
	if form.admin.data:
		user.urole = "ADMIN"
	db.session().add(user)
	db.session().commit()
	
	return redirect(url_for("index"))