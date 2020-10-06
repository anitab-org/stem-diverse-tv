from typing import Dict

def validate_user_signup_data(data: Dict[str, str]):
    if "email" not in data:
        return {'message': "Please enter valid email address"}, 400
    if "username" not in data:
        return {'message': "Please enter valid username"}, 400
    if "name" not in data:
        return {'message': "Please enter valid name"}, 400
    if "password" not in data:
        return {'message': "Please enter valid password"}, 400
    if "terms_and_conditions_checked" not in data:
        return {'message': "Please enter terms and conditions"}, 400
    if data["terms_and_conditions_checked"] == False:
        return {'message': "Please accept terms and conditions in order to register"}, 400
