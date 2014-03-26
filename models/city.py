from mysite import db

class City(db.Model):
	__tablename__ = "City"
	
	id         = db.Column(db.Integer, primary_key=True)
	name       = db.Column(db.String(16), default="")
	provinceId = db.Column(db.Integer, db.ForeignKey("Province.id"))

	province = db.relationship("Province", backref="citys")

	def __init__(self, *args, **kwargs):
		super(City, self).__init__(*args, **kwargs)

	@property
	def serialize(self):
		return {"id":self.id, "name":self.name}