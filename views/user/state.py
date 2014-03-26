from flask import redirect, url_for
from extensions.flask_login import login_required, current_user
from mysite import db
from mysite.models import User
from mysite.decorators import roles_accepted
from . import user

@user.route("/state/<int:uid>")
@login_required
@roles_accepted(current_user, "admin", "hosRole", "depRole")
def state(uid):
	user = User.query.get_or_404(uid)
	if user.state:
		user.state = False
	else:
		user.state = True
	db.session.add(user)
	db.session.commit()
	return redirect(url_for("user.search"))