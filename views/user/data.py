# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, abort, url_for, jsonify
from extensions.flask_login import current_user, login_required
from mysite.models import User
from . import user

@user.route("/data")
@login_required
def data():                         
    return render_template("user/data.html")