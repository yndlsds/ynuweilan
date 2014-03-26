from flask import render_template
from mysite.models import Weixin
from . import weixin

@weixin.route("/search")
def search():
	return render_template("weixin/search.html")