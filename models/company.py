from mysite import db

class Company(db.Model):
	__tablename__ = "Company"
	__searchable__ = ["name", "manager", "brief", "province", "city", "address", "brands", "categorys"]
	
	id        = db.Column(db.Integer, primary_key=True)
	#profile
	name      = db.Column(db.String(16), default="")	
	manager   = db.Column(db.String(8), default="")
	brief     = db.Column(db.String(140), default="")
	#location
	province  = db.Column(db.String(8), default="")
	cityId    = db.Column(db.Integer, db.ForeignKey("City.id"))
	city      = db.Column(db.String(8), default="")
	address   = db.Column(db.String(64), default="")
	#contact
	phone     = db.Column(db.String(11), default="")
	telephone = db.Column(db.String(32), default="")
	qq        = db.Column(db.String(32), default="")
	email     = db.Column(db.String(32), default="")
	website   = db.Column(db.String(32), default="")
	#brand & category
	brands    = db.Column(db.String(255), default="")
	categorys = db.Column(db.String(255), default="")
	#user
	userId    = db.Column(db.Integer, db.ForeignKey("User.id"))
	#state
	state     = db.Column(db.Boolean, default=True)
	
	user = db.relationship("User", backref="company")

	def __init__(self, *args, **kwargs):
		super(Company, self).__init__(*args, **kwargs)

	@property
	def serialize(self):
		return {
			"id"        : self.id,
			"text"      : self.name,
			"name"      : self.name,
			"manager"   : self.manager,
			"phone"     : self.phone,
			"location"  : self.province + " " + self.city.name,
			"brands"    : self.brands,
			"categorys" : self.categorys}