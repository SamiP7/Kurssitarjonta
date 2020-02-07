from flask import render_template
from application import app
from application.topics.models import Topic

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", find_courses=Topic.find_courses_by_topic())