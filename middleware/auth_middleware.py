import jwt, os
from flask import request, g, current_app
from functools import wraps


def user_required(fn):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return {"error": "Unauthorized User"}, 401
        
        try:
            cleanToken = token.split()[1]
            decoded_token = jwt.decode(cleanToken, os.getenv('SECRET'), algorithms="HS256")
            id = decoded_token.get("id")
            if id:
                return current_app.ensure_sync(fn)(id, *args, **kwargs)
            else:
                return {"error": "User access is required"}, 403
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Token i valid"}, 401
    wrapper.__name__ = fn.__name__
    return wrapper

def admin_required(fn):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return {"error": "Unauthorized User"}, 401
        
        try:
            cleanToken = token.split()[1]
            decoded_token = jwt.decode(cleanToken, os.getenv('SECRET'), algorithms="HS256")
            id = decoded_token.get("id")
            role = decoded_token.get("role")
            if role == "admin":
                return current_app.ensure_sync(fn)(id, *args, **kwargs)
            else:
                return {"error": "User access is required"}, 403
        except jwt.ExpiredSignatureError:
            return {"error": "Token has expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Token invalid valid"}, 401
    wrapper.__name__ = fn.__name__
    return wrapper

