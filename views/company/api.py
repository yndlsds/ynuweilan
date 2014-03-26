from flask import request, jsonify
from mysite import db
from mysite.models import Company
from . import company

@company.route("/api")
def api():
	name = request.args.get("q")
	companys = Company.query.filter(db.and_(Company.name.like("%"+name+"%"), Company.state==True)).all()
	return jsonify(results=[company.serialize for company in companys])