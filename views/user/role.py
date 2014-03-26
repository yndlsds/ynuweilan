from flask import redirect, url_for
from extensions.flask_login import login_required, current_user
from mysite import db
from mysite.models import User
from mysite.decorators import role_required
from . import user

@user.route("/role/<int:uid>/manager")
@login_required
@role_required(current_user, "admin")
def manager(uid):
	user = User.query.get_or_404(uid)
	if user.has_role("manager"):
		user.role = ""
	else:
		user.role = "manager"
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("user.search"))