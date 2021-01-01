from flask import request, Response
import json
from app.utils import messages
from flask_restplus import Api, Resource, Namespace, fields, Model
from app.database.models.author import AuthorModel
from app.apis.models.user import *
from firebase_admin import auth
from app.apis.validations.user import validate_user_signup_data
from app.apis.dao.user import UserDAO

user_ns = Namespace('user', description='User related functions')
add_models_to_namespace(user_ns)

@user_ns.route('/register')
class RegisterUser(Resource):
    
    @user_ns.expect(register_user_model)
    def post(self):
        data = request.json
        
        not_valid = validate_user_signup_data(data)
        
        if not_valid:
            return not_valid
        
        result = UserDAO.create_user(data)
        return result
    
@user_ns.route('/login')
class RegisterUser(Resource):
    
    @user_ns.expect(login_user_model)
    def post(self):
        data = request.json
        email = data["email"]
        password = data["password"]
        
        login_response = UserDAO.authenticate(email, password)
        return login_response
