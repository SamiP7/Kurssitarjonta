from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
	email = StringField("Email", [validators.Email(message="Not a valid email")])
	password = PasswordField("Password", [validators.Length(min=5)])
	name = StringField("Name", [validators.Length(min=1)])
	phonenumber = StringField("Phone number(optional)")
	
	class Meta:
		csrf = False