from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TopicForm(FlaskForm):
    name = StringField("Topic name", [validators.Length(min=5)])
 
    class Meta:
        csrf = False