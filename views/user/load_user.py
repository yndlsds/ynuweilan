from mysite import login_manager
from mysite.models import User

@login_manager.user_loader
def load_user(userId):
	return User.query.get(userId)