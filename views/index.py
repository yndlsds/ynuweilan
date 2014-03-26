from flask import redirect, url_for
from mysite import app

@app.route("/")
def index():
	return redirect(url_for("user.home"))