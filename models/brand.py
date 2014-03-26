from mysite import db

class Brand(db.Model):
	__tablename__ = "Brand"
	
	id    = db.Column(db.Integer, primary_key=True)
	name  = db.Column(db.String(8), default="")
	times = db.Column(db.Integer, default=0)
	state = db.Column(db.Boolean, default=True)

	def __init__(self, *args, **kwargs):
		super(Brand, self).__init__(*args, **kwargs)

	@property
	def serialize(self):
		return {"id":self.name, "text":self.name}