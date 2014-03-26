from mysite import db

class Product(db.Model):
	__tablename__ = "Product"
	__searchable__ = ["name", "brief", "brand", "category"]

	id        = db.Column(db.Integer, primary_key=True)
	name      = db.Column(db.String(32), default="")
	brief     = db.Column(db.String(140), default="")
	brand     = db.Column(db.String(8), default="")
	category  = db.Column(db.String(8), default="")
	price     = db.Column(db.Float, default=0.0)
	companyId = db.Column(db.Integer, db.ForeignKey("Company.id"))
	state     = db.Column(db.Boolean, default=True)

	company  = db.relationship("Company", backref="products")
	
	def __init__(self, *args, **kwargs):
		super(Product, self).__init__(*args, **kwargs)