from flask import redirect, render_template, request, url_for

from application import app, db, login_required
from application.topics.models import Topic
from application.courses.models import Course
from application.topics.forms import TopicForm

@app.route("/topics/", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topic.query.all())

@app.route("/topics/new/")
@login_required(role="ADMIN")
def topics_form():
	return render_template("topics/new.html", form = TopicForm())
	
@app.route("/topics/<topic_id>/", methods=["POST"])
@login_required(role="ADMIN")
def delete_topic(topic_id):
	if (Course.query.filter_by(topic_id=topic_id).first() is None):
		Topic.query.filter_by(id=topic_id).delete()
		db.session().commit()
	
	return render_template("topics/list.html", topics = Topic.query.all())
	
	
@app.route("/topics/<topic_id>/rename", methods=["POST"])
@login_required(role="ADMIN")
def rename_topic(topic_id):
	form = TopicForm(request.form)
	
	topic = Topic.query.get(topic_id)
	topicname = Topic(form.name.data)
	
	if not form.validate():
		return render_template("topics/list.html", topics = Topic.query.all(), form = form)
		
	topic.name = topicname.name
	db.session().commit()

	return redirect(url_for("topics_index"))
	
@app.route("/topics/<topic_id>/rename/", methods=["GET"])
@login_required(role="ADMIN")
def rename_topic_index(topic_id):
	form = TopicForm(request.form)
	topic = Topic.query.get(topic_id)
	return render_template("topics/rename.html", form = form, topic = topic)
	
	
@app.route("/topics/", methods=["POST"])
@login_required(role="ADMIN")
def topics_create():
	form = TopicForm(request.form)
	
	if not form.validate():
		return render_template("topics/new.html", form = form)
	
	topic = Topic(form.name.data)

	db.session().add(topic)
	db.session().commit()
  
	return redirect(url_for("topics_index"))