from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, IntegerField, validators

class ReservationForm(FlaskForm):
	accountnumber = StringField("Account number", [validators.Length(min=1)])
	indexnumber = IntegerField("Indexnumber", [validators.NumberRange(min=0)])
	amount = IntegerField("Amount", [validators.NumberRange(min=0, max=1000, message="Only values inbetween 0-1000 are allowed")])
  
	class Meta:
		csrf = False