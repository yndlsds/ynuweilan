from flask import request, jsonify
from mysite import db
from mysite.models import Category
from . import api

@api.route("/category")
def category():
	name = request.args.get("q")
	return jsonify(results=[i.serialize
		for i in Category.query.filter(db.and_(Category.name.like("%"+name+"%"), Category.state==True)).all()])