from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, validators
from application.auth.models import UniqueValidator, User
from wtforms.validators import ValidationError

class LoginForm(FlaskForm):
	email = StringField("Email", [validators.Email(message="Not a valid email"), UniqueValidator(User, User.email)])
	password = PasswordField("Password", [validators.Length(min=5)])
	name = StringField("Name", [validators.Length(min=1)])
	phonenumber = StringField("Phone number(optional)")
	admin = BooleanField("Admin?")
	
	class Meta:
		csrf = False
