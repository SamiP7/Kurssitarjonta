from flask import redirect, render_template, request, url_for
from application import app, db
from application.topics.models import Topic

@app.route("/topics/", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topic.query.all())

@app.route("/topics/new/")
def topics_form():
	return render_template("topics/new.html")
	
@app.route("/topics/<topic_id>/", methods=["POST"])
def delete_topic(topic_id):
	
	Topic.query.filter_by(id=topic_id).delete()
	db.session().commit()
	
	return render_template("topics/list.html", topics = Topic.query.all())
	
	
@app.route("/topics/<topic_id>/rename/", methods=["POST", "GET"])
def rename_topic(topic_id):

	t = Topic.query.get(topic_id)
	a = Topic(request.form.get("name"))
	t.name = a.name
	db.session().commit()

	
	return redirect(url_for("topics_index"))
		
	
@app.route("/topics/", methods=["POST"])
def topics_create():
    t = Topic(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("topics_index"))