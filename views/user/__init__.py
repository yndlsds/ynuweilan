from flask import Blueprint

user = Blueprint("user", __name__)

from data import data
from home import home
from load_user import load_user
from login import login_email, login_weixin, login_weixin_check
from logout import logout
from register import register
from role import manager
from search import search
from state import state