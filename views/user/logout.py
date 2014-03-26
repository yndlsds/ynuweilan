# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, session, current_app
from extensions.flask_login import logout_user
from . import user

@user.route("/logout")
def logout():
    logout_user()
    flash(u"注销成功", "success")
    return redirect(url_for("index"))