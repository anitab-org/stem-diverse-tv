from flask_restplus import Model, fields


def add_models_to_namespace(api_namespace):
    api_namespace.models[add_category_sections.name] = add_category_sections


add_category_sections = Model(
    "Fields needed for adding new category sections instances",
    {
        "sections": fields.List(fields.Integer(), description="list of section ids"),
    },
)
