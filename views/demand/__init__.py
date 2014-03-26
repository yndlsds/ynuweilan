from flask import Blueprint

demand = Blueprint("demand", __name__)

from search import search
from state import state