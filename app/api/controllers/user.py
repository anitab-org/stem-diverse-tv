from flask import request
from flask_restplus import Resource, Namespace

from app.api.dao.user_dao import UserDAO
from app.api.models.user import *
from app.api.validations.user import validate_user_signup_data

user_ns = Namespace("users", description="User related functions")
add_models_to_namespace(user_ns)


@user_ns.route("/register")
class RegisterUser(Resource):
    @user_ns.expect(register_user_model)
    def post(self):
        data = request.json
        not_valid = validate_user_signup_data(data)
        if not_valid:
            return not_valid

        result = UserDAO.create_user(data)
        return result


@user_ns.route("/login")
class RegisterUser(Resource):
    @user_ns.expect(login_user_model)
    def post(self):
        data = request.json
        email = data["email"]
        password = data["password"]
        login_response = UserDAO.authenticate(email, password)
        return login_response
