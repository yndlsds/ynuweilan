# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, abort, url_for, jsonify
from extensions.flask_login import current_user, login_user
from extensions.randomword import randomword
# from mysite import mc
from mysite.forms import UserForm
from mysite.models import User
from . import user

@user.route("/login/email", methods=["GET", "POST"])
def login_email():
    if current_user.is_authenticated():
        flash(u"已经有一个用户登陆了！", "warning")
        return redirect(url_for("user.home"))
        
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=str(form.email.data)).first()
        if user:
            if user.check_password(form.password.data):
                user.update_login_date()
                login_user(user)
                flash(u"欢迎回来！", "success")
                return redirect(request.args.get("next") or url_for("user.home"))
            else:
                flash(u"邮箱和密码不匹配，请重试！", "danger")
                return redirect(url_for("user.login_email"))
        else:
            flash(u"用户不存在，请注册！", "warning")
            return redirect(url_for("user.register"))                            
    return render_template("user/login_email.html", form=form)

@user.route("/login/weixin")
def login_weixin():
    if current_user.is_authenticated():
        flash(u"已经有一个用户登陆了！", "warning")
        return redirect(url_for("user.home"))
    random = randomword(6)
    # mc.set(random, "")                        
    return render_template("user/login_weixin.html", random=random)

@user.route("/login/weixin/check/<path:random>")
def login_weixin_check(random):
    # openid = mc.get(str(random))
    if openid:
        # mc.delete(random)
        user = User.query.filter_by(openid=openid).first_or_404()
        user.update_login_date()
        login_user(user)        
        flash(u"欢迎回来", "success")
        return jsonify(success=True)
    else:
        return jsonify(success=False)