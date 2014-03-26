from flask import render_template
from extensions.flask_login import login_required, current_user
from mysite import db
from mysite.models import User
from . import user

@user.route("/search")
@login_required
def search():
	if current_user.has_role("admin"):
		users = User.query.all()
	if current_user.has_role("hosRole"):
		users = User.query.filter(db.or_(User.role=="depRole", User.role=="")).all()
	if current_user.has_role("depRole"):
		users = User.query.filter_by(role="").all()
	if current_user.has_role(""):
		users = [current_user]
	return render_template("user/search.html", users=users)