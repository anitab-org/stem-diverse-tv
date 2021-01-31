from flask import request, Response
import os
import json
import requests
from urllib.parse import urlparse, parse_qs
from flask_restplus import Api, Resource, Namespace, reqparse, marshal
from app.apis.dao.section_dao import SectionDAO
from app.database.models.category import CategoryModel
from app.apis.models.video import *
from app.apis.validations.video import validate_video_creation_data
from app.apis.dao.video_dao import VideoDAO
from app.apis.dao.author_dao import AuthorDAO
from datetime import datetime
from ..mappers.video_mapper import map_to_dto
from .middlewares.auth import token_required

video_ns = Namespace("video", description="Video Library")
add_models_to_namespace(video_ns)


def extract_video_id(url):
    # Examples:
    # - http://youtu.be/SA2iWivDJiE
    # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    # - http://www.youtube.com/embed/SA2iWivDJiE
    # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    query = urlparse(url)
    if query.hostname == "youtu.be":
        return query.path[1:]
    if query.hostname in {"www.youtube.com", "youtube.com"}:
        if query.path == "/watch":
            return parse_qs(query.query)["v"][0]
        if query.path[:7] == "/embed/":
            return query.path.split("/")[2]
        if query.path[:3] == "/v/":
            return query.path.split("/")[2]
    # fail?
    return None


yt_video_section_field = video_ns.model(
    "Section",
    {
        "title": fields.String(required=True),
        "category": fields.String,
        "id": fields.String(required=True),
    },
)

# yt_video_section_id_field = video_ns.model(
#     "Existing Section Id", {"id": fields.String(required=True)}
# )

add_yt_video_fields = video_ns.model(
    "Add Youtube Video Fields",
    {
        "url": fields.String(
            description="YouTube video url",
            required=True,
            default="http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu",
        ),
        "sections": fields.List(fields.Nested(yt_video_section_field)),
        "authors": fields.List(fields.Integer(description="existing author id")),
    },
)


@video_ns.route("/add_category")
class AddCategory(Resource):
    @token_required
    @video_ns.doc(params={"title": "Title of category"})
    @video_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def post(self):
        args = request.args
        title = args["title"]
        existing_category = CategoryModel.find_by_title(title)
        if existing_category:
            return {"message": "Category already exists"}, 409

        """ Saving title in capitalized letter. Which can prevent inconsistency in finding existing category title. """
        category = CategoryModel(title.capitalize())
        category.save_to_db()

        return {"message": "Category added"}, 201


@video_ns.route("/latest")
class VideoLibrary(Resource):
    @token_required
    @video_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def get(self):
        with open("./content/latests.json") as f:
            return json.loads(f.read())
        return jsonify({"message": "File does not exist."})


@video_ns.route("/")
class Video(Resource):
    @token_required
    @video_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    @video_ns.expect(add_video_model)
    def post(self):
        data = request.json
        validation_result = validate_video_creation_data(data)

        if validation_result is not None:
            return validation_result
        url = data["url"]
        existing_video = VideoDAO.find_video_by_url(url)
        response = {"notes": []}

        # find authors from the list
        authors = AuthorDAO.find_authors_by_ids(data["authors"])
        if authors.count() != len(data["authors"]):
            response["notes"].append(
                "Some of the authors are not valid or they do not exist."
            )

        # find sections from the list
        sections = SectionDAO.find_sections_by_ids(data["category_sections"])
        if sections.count() != len(data["category_sections"]):
            response["notes"].append(
                "Some of the sections are not valid or they do not exist."
            )

        # remove association fields
        data.pop("authors")
        data.pop("category_sections")

        if existing_video:
            data["date_published"] = datetime.strptime(
                data["date_published"], "%Y-%m-%d"
            )
            existing_video.update(data)
            VideoDAO.replace_video_authors(existing_video, authors)
            VideoDAO.replace_video_sections(existing_video, sections)
            video = existing_video
        else:
            video = VideoDAO.create_video(
                data["title"],
                data["url"],
                data["preview_url"],
                datetime.strptime(data["date_published"], "%Y-%m-%d"),
                data["source"],
                data["channel"],
                data["duration"],
                data.get("archived"),
                data.get("free_to_reuse"),
                data.get("authorized_to_reuse"),
            )
            VideoDAO.add_video_authors(video, authors)
            VideoDAO.add_video_sections(video, sections)

        response["video"] = map_to_dto(video)
        return response, 200


@video_ns.route("/youtube")
class AddYoutubeVideo(Resource):
    @token_required
    @video_ns.expect(add_yt_video_fields)
    def post(self):
        payload = request.json
        video_url = payload["url"]
        video_id = extract_video_id(video_url)
        searchResult = requests.get(
            f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cid%2Clocalizations%2Cstatistics%2CtopicDetails&id={video_id}&key={os.environ.get("API_KEY")}'
        )
        result = searchResult.json()
        # datePublished = result["items"][0]["snippet"]["publishedAt"]
        # formattedDate = datePublished.split("T")[0]
        video_data = {
            "title": result["items"][0]["snippet"]["title"],
            "url": video_url,
            "preview_url": result["items"][0]["snippet"]["thumbnails"]["standard"][
                "url"
            ],
            "date_published": result["items"][0]["snippet"]["publishedAt"].split("T")[
                0
            ],
            "source": "YouTube",
            "channel": result["items"][0]["snippet"]["channelTitle"],
            "duration": result["items"][0]["contentDetails"]["duration"].split("T")[1],
            "archived": False,
            "free_to_reuse": result["items"][0]["contentDetails"]["licensedContent"],
            "authorized_to_reuse": result["items"][0]["contentDetails"][
                "licensedContent"
            ],
            "category_sections": payload["sections"][0]["id"],
            "authors": list(payload["authors"]),
        }

        validation_result = validate_video_creation_data(video_data)

        if validation_result is not None:
            return validation_result
        url = video_data["url"]
        existing_video = VideoDAO.find_video_by_url(url)
        response = {"notes": []}

        # find authors from the list
        authors = AuthorDAO.find_authors_by_ids(video_data["authors"])
        if authors.count() != len(video_data["authors"]):
            response["notes"].append(
                "Some of the authors are not valid or they do not exist."
            )

        # find sections from the list
        sections = SectionDAO.find_sections_by_ids(video_data["category_sections"])
        if sections.count() != len(video_data["category_sections"]):
            response["notes"].append(
                "Some of the sections are not valid or they do not exist."
            )

        # remove association fields
        video_data.pop("authors")
        video_data.pop("category_sections")

        if existing_video:
            video_data["date_published"] = datetime.strptime(
                video_data["date_published"], "%Y-%m-%d"
            )
            existing_video.update(video_data)
            VideoDAO.replace_video_authors(existing_video, authors)
            VideoDAO.replace_video_sections(existing_video, sections)
            video = existing_video
        else:
            video = VideoDAO.create_video(
                video_data["title"],
                video_data["url"],
                video_data["preview_url"],
                datetime.strptime(video_data["date_published"], "%Y-%m-%d"),
                video_data["source"],
                video_data["channel"],
                video_data["duration"],
                video_data.get("archived"),
                video_data.get("free_to_reuse"),
                video_data.get("authorized_to_reuse"),
            )
            VideoDAO.add_video_authors(video, authors)
            VideoDAO.add_video_sections(video, sections)

        response["video"] = map_to_dto(video)
        return response, 200
