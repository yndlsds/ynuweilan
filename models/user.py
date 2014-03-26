from datetime import datetime
import hashlib
from extensions.flask_login import UserMixin
from mysite import db

class User(db.Model, UserMixin):
	__tablename__ = "User"
	
	id        = db.Column(db.Integer, primary_key=True)
	# weixin
	weixinhao = db.Column(db.String(16), default="")
	openid    = db.Column(db.String(64), default="")
	# email account
	email     = db.Column(db.String(32), default="")
	_password = db.Column(db.String(32), default="")
	role      = db.Column(db.String(8), default="")
	# date
	register  = db.Column(db.DateTime, default=datetime.now())
	login     = db.Column(db.DateTime, default=datetime.now())
	# account
	account   = db.Column(db.Integer, default=0)
	# state
	state     = db.Column(db.Boolean, default=True)

	def __init__(self, *args, **kwargs):
		super(User, self).__init__(*args, **kwargs)

	def set_password(self, password):
		self._password = hashlib.md5(password).hexdigest()

	def check_password(self, password):
		return self._password == hashlib.md5(password).hexdigest()

	def update_login_date(self):
		self.login = datetime.now()
		db.session.add(self)
		db.session.commit()

	def has_role(self, role):
		return role == self.role