from flask import redirect, url_for
from extensions.flask_login import login_required, current_user
from mysite import db
from mysite.models import Demand
from mysite.decorators import roles_accepted
from . import demand

@demand.route("/state/<int:demandId>")
@login_required
@roles_accepted(current_user, "admin", "manager")
def state(demandId):
	demand = Demand.query.get_or_404(demandId)
	if demand.state:
		demand.state = False
	else:
		demand.state = True
	db.session.add(demand)
	db.session.commit()
	return redirect(url_for("demand.search"))