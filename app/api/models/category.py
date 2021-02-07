from flask_restplus import Model, fields


def add_models_to_namespace(api_namespace):
    api_namespace.models[add_category_sections.name] = add_category_sections
    api_namespace.models[update_category_model.name] = update_category_model


add_category_sections = Model(
    "Fields needed for adding new category sections instances",
    {
        "sections": fields.List(fields.Integer(), description="list of section ids"),
    },
)

update_category_model = Model(
    "Fields required for updating a category",
    {"title": fields.String(required=True, description="category title")}
)
