from flask import render_template
from mysite.models import Company
from . import company

@company.route("/preview")
@company.route("/preview/<int:companyId>")
def preview(companyId=1):
    company = Company.query.get_or_404(companyId)
    return render_template("company/preview.html", company=company)