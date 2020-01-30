from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
	email = StringField("Email")
	password = PasswordField("Password")
	name = StringField("Name")
	phonenumber = StringField("Phone number")
	
	class Meta:
		csrf = False