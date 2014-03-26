import hashlib
from mysite import db

class Weixin(db.Model):
	__tablename__ = "Weixin"
	
	id     = db.Column(db.Integer, primary_key=True)
	name   = db.Column(db.String(32))
	random = db.Column(db.String(8))
	userId = db.Column(db.Integer, db.ForeignKey("User.id"))
	state  = db.Column(db.Boolean, default=True)

	user = db.relationship("User", backref="weixin", uselist=False)

	def __init__(self, *args, **kwargs):
		super(Weixin, self).__init__(*args, **kwargs)

	def __str__(self):
		return self.name