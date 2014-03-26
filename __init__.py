# -*- coding: utf-8 -*-
#flask
from flask import Flask
app = Flask(__name__)
app.config.from_object("mysite.config")

#flask-sqlalchemy
from extensions.flask_sqlalchemy import SQLAlchemy
class nullpool_SQLAlchemy(SQLAlchemy): 
	def apply_driver_hacks(self, app, info, options): 
		super(nullpool_SQLAlchemy, self).apply_driver_hacks(app, info, options) 
		from sqlalchemy.pool import NullPool 
		options["poolclass"] = NullPool 
		del options["pool_size"] 
db = nullpool_SQLAlchemy(app)

#flask-login
from extensions.flask_login import LoginManager
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "user.login_email"
login_manager.login_message = u"如需继续操作，请登录！"
login_manager.login_message_category = u"warning"

#sae memcache
# import pylibmc
# mc = pylibmc.Client()

import models
import views

#register blueprint
app.register_blueprint(views.api, url_prefix="/api")
app.register_blueprint(views.company, url_prefix="/company")
app.register_blueprint(views.demand, url_prefix="/demand")
app.register_blueprint(views.user, url_prefix="/user")
app.register_blueprint(views.weixin, url_prefix="/weixin")

#create whoosh index
from flask.ext.whooshalchemy import whoosh_index
whoosh_index(app, models.Company)
whoosh_index(app, models.Demand)
whoosh_index(app, models.Product)