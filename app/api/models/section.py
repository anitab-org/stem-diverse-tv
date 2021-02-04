from flask_restplus import Model, fields


def add_models_to_namespace(api_namespace):
    api_namespace.models[add_section_model.name] = add_section_model
    api_namespace.models[update_section_model.name] = update_section_model


add_section_model = Model(
    "Fields needed for adding new section",
    {
        "title": fields.String(required=True, description="section title"),
        "category": fields.String(required=True, description="category of the section"),
    },
)

update_section_model = Model(
    "Fields needed for updating an existing section",
    {
        "title": fields.String(required=True, description="section title")
    },
)