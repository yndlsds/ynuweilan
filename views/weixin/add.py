# -*- coding: utf-8 -*-
from flask import request, render_template, flash, redirect, url_for
from extensions.flask_login import login_required, current_user
from extensions.randomword import randomword
from mysite import db
from mysite.forms import WeixinForm
from mysite.models import Weixin
from . import weixin

@weixin.route("/add", methods = ["GET", "POST"])
@login_required
def add():
	if current_user.weixin:
		flash(u"您已经绑定了微信公众号", "warning")
		return redirect(url_for("weixin.edit"))

	weixin = Weixin()
	form = WeixinForm(request.form)
	if request.method == "POST" and form.validate():
		form.populate_obj(weixin)
		weixin.user = current_user
		weixin.random = randomword(8)
		db.session.add(weixin)
		db.session.commit()
		flash(u"新建成功", "success")
		return redirect(url_for("user.home"))
	return render_template("weixin/form.html", form=form)