from flask import request, Response
import json
from firebase_admin import auth
from functools import wraps
import app.utils.messages as msg
 
def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token_header = request.headers['authorization']
        
        try:
            decoded_token = auth.verify_id_token(token_header)
            
        except auth.RevokedIdTokenError as ex:
            return msg.TOKEN_REVOKED, 400
        except auth.ExpiredIdTokenError as ex:
            return msg.TOKEN_EXPIRED, 400
        except auth.InvalidIdTokenError as ex:
            return msg.TOKEN_INVALID, 400
        
        return fn(*args, **kwargs)
    return wrapper
