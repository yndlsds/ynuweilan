# -*- coding: utf-8 -*-
from wtforms import Form, TextField, PasswordField
from wtforms.validators import Required, Length, Email

class UserForm(Form):
	email    = TextField("email", [Required(message=u"必填"), Length(max=32, message=u"不能超过32个字符"), Email(message="不是邮箱地址")])
	password = PasswordField("password", [Required(message=u"必填"), Length(max=8, message=u"不能超过8个字符")])