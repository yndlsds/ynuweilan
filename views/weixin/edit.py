# -*- coding: utf-8 -*-
from flask import request, render_template, flash, redirect, url_for
from extensions.flask_login import current_user, login_required
from mysite import db
from mysite.models import Weixin
from mysite.forms import WeixinForm
from . import weixin

@weixin.route("/edit", methods = ["GET", "POST"])
@login_required
def edit():
	if not current_user.weixin:
		flash(u"您还没绑定微信公众号", "warning")
		return redirect(url_for("weixin.add"))

	weixin = Weixin.query.filter_by(user=current_user).first_or_404()
	form = WeixinForm(request.form, obj=weixin)
	if request.method == "POST" and form.validate():
		form.populate_obj(weixin)
		db.session.add(weixin)
		db.session.commit()
		flash(u"修改成功", "success")
		return redirect(url_for("user.home"))
	return render_template("weixin/form.html", form=form)