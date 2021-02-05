from flask_restplus import Model, fields


def add_models_to_namespace(api_namespace):
    api_namespace.models[update_category_model.name] = update_category_model


update_category_model = Model(
    "Fields required for updating a category",
    {"title": fields.String(required=True, description="category title")},
)
