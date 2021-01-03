from flask_restplus import fields, Model


def add_models_to_namespace(api_namespace):
    api_namespace.models[register_user_model.name] = register_user_model
    api_namespace.models[login_user_model.name] = login_user_model


register_user_model = Model(
    "Fields needed for user registration",
    {
        "name": fields.String(required=True, description="Name of user"),
        "username": fields.String(required=True, description="Username of user"),
        "email": fields.String(required=True, description="Email of user"),
        "password": fields.String(required=True, description="Password of user"),
        "terms_and_conditions_checked": fields.Boolean(required=True,
                                                       description="Wether terms and conditions are checked"),
    }
)

login_user_model = Model(
    "Fields needed for user login",
    {
        "email": fields.String(required=True, description="email of user"),
        "password": fields.String(required=True, description="password of user")
    }
)
