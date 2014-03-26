from flask import redirect, url_for
from extensions.flask_login import login_required, current_user
from mysite import db
from mysite.models import Company
from mysite.decorators import roles_accepted
from . import company

@company.route("/state/<int:companyId>")
@login_required
@roles_accepted(current_user, "admin", "manager")
def state(companyId):
	company = Company.query.get_or_404(companyId)
	if company.state:
		company.state = False
	else:
		company.state = True
	db.session.add(company)
	db.session.commit()
	return redirect(url_for("company.search"))