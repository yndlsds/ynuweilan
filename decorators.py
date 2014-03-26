from functools import wraps
from flask import abort

def role_required(user, role):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if user.role != role:
                return abort(403)
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

def roles_accepted(user, *roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if user.role not in roles:
                return abort(403)
            return fn(*args, **kwargs)            
        return decorated_view
    return wrapper