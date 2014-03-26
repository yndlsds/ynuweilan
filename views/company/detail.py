from flask import render_template
from mysite.models import Company
from . import company

@company.route("/")
@company.route("/<int:companyId>")
def detail(companyId=1):
    company = Company.query.get_or_404(companyId)
    return render_template("company/detail.html", company=company)