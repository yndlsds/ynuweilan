from flask import render_template
from extensions.flask_login import login_required
from mysite.models import Demand
from . import demand

@demand.route("/search")
@demand.route("/search/<int:page>")
@login_required
def search(page=1):
	demands = Demand.query.paginate(page, per_page=100, error_out=False)
	return render_template("demand/search.html", demands=demands)