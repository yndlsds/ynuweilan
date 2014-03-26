from flask import render_template
from extensions.flask_login import login_required
from . import user

@user.route("/")
@login_required
def home():
	return render_template("user/home.html")