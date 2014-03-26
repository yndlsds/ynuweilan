from flask import Blueprint

company = Blueprint("company", __name__)

from api import api
from detail import detail
from edit import edit
from preview import preview
from search import search
from state import state