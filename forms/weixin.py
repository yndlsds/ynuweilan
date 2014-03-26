# -*- coding: utf-8 -*-
from wtforms import Form, TextField
from wtforms.validators import Required, Length

class WeixinForm(Form):
	name = TextField("name", [Required(message=u"必填"), Length(max=32, message=u"不能超过32个字符")])
	