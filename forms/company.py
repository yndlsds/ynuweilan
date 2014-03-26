# -*- coding: utf-8 -*-
from wtforms import Form, TextField, TextAreaField
from wtforms.validators import Required, Length

class CompanyForm(Form):
	#profile
	name       = TextField("name", [Required(message="必填"), Length(max=16, message="不能超过16个字符")])	
	manager    = TextField("manager", [Required(message="必填"), Length(max=8, message="不能超过8个字符")])
	brief      = TextAreaField("brief", [Length(max=140, message="不能超过140个字符")])
	#location
	address    = TextField("address", [Required(message="必填"), Length(max=64, message="不能超过64个字符")])
	#contact
	phone      = TextField("phone", [Required(message="必填"), Length(max=11, message="不能超过11个字符")])
	telephone  = TextField("telephone", [Length(max=32, message="不能超过32个字符")])
	qq         = TextField("qq", [Length(max=32, message="不能超过32个字符")])
	email      = TextField("email", [Length(max=32, message="不能超过32个字符")])
	website    = TextField("website", [Length(max=32, message="不能超过32个字符")])
	#brand & category
	brands     = TextField("brands", [Length(max=255, message="不能超过255个字符")])
	categorys  = TextField("categorys", [Length(max=255, message="不能超过255个字符")])