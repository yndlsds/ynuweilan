from datetime import datetime
from mysite import db

class Charge(db.Model):
	__tablename__ = "Charge"
	
	id       = db.Column(db.Integer, primary_key=True)
	name     = db.Column(db.String(8), unique=True)
	number   = db.Column(db.Integer, default=0)
	userId   = db.Column(db.Integer, db.ForeignKey("User.id"))
	datetime = db.Column(db.DateTime, default=datetime.now())
	state    = db.Column(db.Boolean, default=True)

	user = db.relationship("User", backref="charges")

	def __init__(self, *args, **kwargs):
		super(Charge, self).__init__(*args, **kwargs)