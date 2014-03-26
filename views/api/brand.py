from flask import request, jsonify
from mysite import db
from mysite.models import Brand
from . import api

@api.route("/brand")
def brand():
	name = request.args.get("q")
	return jsonify(results=[i.serialize
		for i in Brand.query.filter(db.and_(Brand.name.like("%"+name+"%"), Brand.state==True)).all()])