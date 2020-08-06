from flask_restplus import fields, Model

add_author_model = Model(
    "Add author Model",
    {
        "name": fields.String(required=True, description="Name of author"),
        "profile_image": fields.String(required=False, description="Author photo url")
    }
)
