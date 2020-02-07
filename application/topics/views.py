from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.topics.models import Topic
from application.topics.forms import TopicForm

@app.route("/topics/", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topic.query.all())

@app.route("/topics/new/")
@login_required
def topics_form():
	return render_template("topics/new.html", form = TopicForm())
	
@app.route("/topics/<topic_id>/", methods=["POST"])
@login_required
def delete_topic(topic_id):
	
	Topic.query.filter_by(id=topic_id).delete()
	db.session().commit()
	
	return render_template("topics/list.html", topics = Topic.query.all())
	
	
@app.route("/topics/<topic_id>/rename/", methods=["POST", "GET"])
@login_required
def rename_topic(topic_id):
	form = TopicForm(request.form)
	
	topic = Topic.query.get(topic_id)
	topicname = Topic(form.name.data)
	
	if not form.validate():
		return render_template("topics/list.html", topics = Topic.query.all(), form = form)
		
	topic.name = topicname.name
	db.session().commit()

	return redirect(url_for("topics_index"))
		
	
@app.route("/topics/", methods=["POST"])
@login_required
def topics_create():
	form = TopicForm(request.form)
	
	if not form.validate():
		return render_template("topics/new.html", form = form)
	
	topic = Topic(form.name.data)

	db.session().add(topic)
	db.session().commit()
  
	return redirect(url_for("topics_index"))