from flask_restplus import Model, fields


def add_models_to_namespace(api_namespace):
    api_namespace.models[add_video_model.name] = add_video_model
    api_namespace.models[add_yt_video_model.name] = add_yt_video_model
    api_namespace.models[add_video_sections.name] = add_video_sections


add_video_model = Model(
    "Fields needed for adding new video",
    {
        "title": fields.String(required=True, description="video title"),
        "url": fields.String(required=True, description="video url"),
        "preview_url": fields.String(required=True, description="video preview url"),
        "date_published": fields.Date(required=True, description="date of publishing"),
        "source": fields.String(required=True, description="video source"),
        "channel": fields.String(required=True, description="video channel"),
        "duration": fields.Integer(
            required=True, description="video duration in seconds"
        ),
        "archived": fields.Boolean(
            required=False, default=False, description="is video archived"
        ),
        "free_to_reuse": fields.Boolean(
            required=False, default=True, description="is video free to reuse"
        ),
        "authorized_to_reuse": fields.Boolean(
            required=False, default=True, description="video authorization permission"
        ),
        "category_sections": fields.List(
            fields.Integer(), description="list of category sections ids"
        ),
        "authors": fields.List(fields.Integer(), description="list of authors ids"),
    },
)

add_yt_video_model = Model(
    "Fields needed for adding new Youtube Video",
    {
        "url": fields.String(
            description="YouTube video url",
            required=True,
        ),
    },
)

add_video_sections = Model(
    "Fields needed for adding new video sections instances",
    {
        "sections": fields.List(fields.Integer(), description="list of section ids"),
    },
)
