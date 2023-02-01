# store standrd roots for webpages, home page, cv,project

# stores list of urls
from flask import Blueprint,render_template

# define blueprint
views = Blueprint("views", __name__)

# define route/blueprint for home page to be registered in init py file 
#decoratotr
@views.route("/")
def profile():
    return render_template("profile.html")
# runs everything inside home

# define route/blueprint for home page to be registered in init py file 
#decoratotr
@views.route("/experience")
def experience():
    return render_template("experience.html")
# runs everything inside home

# define route/blueprint for home page to be registered in init py file 
#decoratotr
@views.route("/projects")
def projects():
    return render_template("projects.html")
# runs everything inside home

# define route/blueprint for home page to be registered in init py file 
#decoratotr
@views.route("/contact")
def contact():
    return render_template("contact.html")
# runs everything inside home


