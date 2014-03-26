#-- flask --
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = "\xa5\xdbFh~\xe9\x07\xcc'\x81\xb2#\x1c\xffS\x01\x07s\xb3\xfbj\xa33\xf8"
STATIC_URL_ROOT = "//static/"

#-- mysql --
# SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:123888@localhost/itdb?charset=utf8"

import os
WHOOSH_BASE = os.path.join(os.path.dirname(__file__), "search.db")