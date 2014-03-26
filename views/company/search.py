from flask import request, render_template, jsonify
from extensions.flask_login import current_user
from mysite import db
from mysite.models import Company, Brand, Category
from . import company

@company.route("/search")
@company.route("/search/<int:page>")
def search(page=1):
	if current_user.has_role("admin") or current_user.has_role("manager"):
		companys = Company.query.paginate(page, per_page=100, error_out=False)
		return render_template("company/admin.html", companys=companys)
	return render_template("company/search.html")

@company.route("/search/name")
def search_name():
	companyId = request.args.get("q")
	companys = Company.query.filter(db.and_(Company.id==companyId, Company.state==True)).all()
	return jsonify(results=[company.serialize for company in companys])

@company.route("/search/city")
def search_city():
	cityId = request.args.get("q")
	companys = Company.query.filter(db.and_(Company.cityId==cityId, Company.state==True)).all()
	return jsonify(results=[company.serialize for company in companys])

@company.route("/search/brand")
def search_brand():
	brand = request.args.get("q")
	companys = Company.query.filter(db.and_(Company.brands.any(Brand.id==brand), Company.state==True)).all()
	return jsonify(results=[company.serialize for company in companys])

@company.route("/search/category")
def search_category():
	category = request.args.get("q")
	companys = Company.query.filter(db.and_(Company.categorys.any(Category.id==category), Company.state==True)).all()
	return jsonify(results=[company.serialize for company in companys])