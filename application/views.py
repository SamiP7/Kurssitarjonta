from flask import render_template, request
from application import app
from application.topics.models import Topic

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", all_topics=Topic.all_topics())
	
@app.route("/search", methods=["GET", "POST"])
def search():
	name = request.form.get("option")
	return render_template("coursesbytopic.html", find_courses=Topic.find_courses_by_topic(name))