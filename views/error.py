# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for
from mysite import app

# -- 404 Not Found --
@app.errorhandler(404)
# -- 403 Forbidden --
@app.errorhandler(403)
# -- 500 Internal Server Error --
@app.errorhandler(500)
def error(e):
	code = getattr(e, "code", 500)
	if code == 404:
		flash(u"404错误 系统未找到！", "danger")
	if code == 403:
		flash(u"403错误 您刚才的操作权限不够！", "danger")
	if code == 500:
		flash(u"500错误 系统内部错误，请联系管理员！", "danger")
	return redirect(url_for("index"))