# -*- coding: utf-8 -*-
from flask import request, flash, redirect, render_template, abort, url_for
from extensions.flask_login import current_user, login_user
from mysite import db
from mysite.forms import UserForm
from mysite.models import User
from . import user

@user.route("/register", methods=["GET", "POST"])
def register():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash(u"该邮箱已被注册过了，请登录", "warning")
            return redirect(url_for("user.login_phone"))
        else:
            user = User(email=form.email.data)
            user.set_password(form.password.data)            
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash(u"注册成功，系统已为您自动登录", "success")
            return redirect(request.args.get("next") or url_for("index"))
    return render_template("user/register.html", form=form)