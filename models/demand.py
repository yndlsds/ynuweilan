from datetime import datetime
from mysite import db

class Demand(db.Model):
	__tablename__ = "Demand"
	__searchable__ = ["content"]
	
	id       = db.Column(db.Integer, primary_key=True)
	content  = db.Column(db.String(140))
	userId   = db.Column(db.Integer, db.ForeignKey("User.id"))
	datetime = db.Column(db.DateTime, default=datetime.now())
	state    = db.Column(db.Boolean, default=True)

	user = db.relationship("User", backref="demands")

	def __init__(self, *args, **kwargs):
		super(Demand, self).__init__(*args, **kwargs)