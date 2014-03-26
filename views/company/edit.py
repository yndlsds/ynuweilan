# -*- coding: utf-8 -*-
from flask import request, render_template, flash, redirect, url_for
from extensions.flask_login import current_user, login_required
from mysite import db
from mysite.models import Company, Province, City
from mysite.forms import CompanyForm
from . import company

@company.route("/edit", methods = ["GET", "POST"])
@login_required
def edit():
    try:
        company = current_user.company[0]
    except IndexError:
        company = Company()
        company.cityId = ""
        company.city = u"城市/区"
        company.user = current_user
    form = CompanyForm(request.form, obj=company)
    print form.brands.data
    if request.method == "POST" and form.validate():
        form.populate_obj(company)
        company.cityId = request.form["cityId"]
        city = City.query.get_or_404(company.cityId)
        company.province = city.province.name
        company.city = city.name
        db.session.add(company)
        db.session.commit()
        flash(u"提交成功", "success")
        return redirect(url_for("user.home"))
    return render_template("company/form.html", company=company, form=form)