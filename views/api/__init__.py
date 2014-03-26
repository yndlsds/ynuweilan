from flask import Blueprint

api = Blueprint("api", __name__)

from brand import brand
from category import category
from city import city