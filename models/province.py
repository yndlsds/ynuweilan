from mysite import db

class Province(db.Model):
	__tablename__ = "Province"
	
	id     = db.Column(db.Integer, primary_key=True)
	name   = db.Column(db.String(8), default="")
	pinyin = db.Column(db.String(8), default="")

	def __init__(self, *args, **kwargs):
		super(Province, self).__init__(*args, **kwargs)

	def __str__(self):
		return self.name