from flask import request
from mysite.models import Weixin
from . import weixin
from ._verification import verification

@weixin.route("/<path:weixinhao>")
def verify(weixinhao):
	weixin = Weixin.query.filter_by(name=weixinhao).first_or_404()
	echostr = request.args.get("echostr")
	if verification(request, weixin.random) and echostr is not None:
		return echostr
	return "access verification fail"