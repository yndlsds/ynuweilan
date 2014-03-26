from flask import Blueprint

weixin = Blueprint("weixin", __name__)

from add import add
from edit import edit
from forward import forward
from verify import verify
from search import search