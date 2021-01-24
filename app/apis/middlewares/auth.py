from flask import request
from firebase_admin import auth
from functools import wraps
import app.utils.messages as msg


def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token_header = request.headers.get('authorization')
        if not token_header:
            return msg.TOKEN_MISSING, 401
        try:
            auth.verify_id_token(token_header)
        except auth.RevokedIdTokenError as ex:
            return msg.TOKEN_REVOKED, 401
        except auth.ExpiredIdTokenError as ex:
            return msg.TOKEN_EXPIRED, 401
        except auth.InvalidIdTokenError as ex:
            return msg.TOKEN_INVALID, 401

        return fn(*args, **kwargs)
    return wrapper
