from flask_restplus import fields, Model


def add_models_to_namespace(api_namespace):
    api_namespace.models[add_author_model.name] = add_author_model


add_author_model = Model(
    "Add author Model",
    {
        "name": fields.String(required=True, description="Name of author"),
        "profile_image": fields.String(required=False, description="Author photo url"),
    },
)
