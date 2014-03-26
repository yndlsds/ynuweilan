# -*- coding: utf-8 -*-
from flask import request, jsonify
from mysite.models import City
from . import api

@api.route("/city")
def city():
	provinceId = request.args.get("provinceId")
	return jsonify(City.query.with_entities(City.id, City.name).filter_by(provinceId=int(provinceId)).all())