import json
import os
from datetime import datetime

import requests
import youtube_dl
from app.api.dao.author_dao import AuthorDAO
from app.api.dao.section_dao import SectionDAO
from app.api.dao.video_dao import VideoDAO
from app.api.middlewares.auth import token_required
from app.api.models.video import *
from app.api.validations.video import (
    validate_video_creation_data,
    validate_video_sections_data,
)
from app.utils.extract_video_id import extract_video_id
from app.utils.youtube_dl import *
from app.utils.messages import RESOURCE_NOT_FOUND
from flask import Response, jsonify, request
from flask_restplus import Api, Namespace, Resource

from ..mappers.video_mapper import map_to_dto

video_ns = Namespace("videos", description="Video Library")
add_models_to_namespace(video_ns)


@video_ns.route("/latest")
class VideoLibrary(Resource):
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
    @video_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    @video_ns.expect(add_yt_video_model)
    def post(self):
        payload = request.json
        video_url = payload["url"]
        video_id = extract_video_id(video_url)
        response = requests.get(
            f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cid%2Clocalizations%2Cstatistics%2CtopicDetails&id={video_id}&key={os.environ.get("API_KEY")}'
        )
        video_json = response.json()
        response = {"notes": []}
        if len(video_json["items"]) == 0:
            response["notes"].append("No video found, please check the url.")
            return response, 404
        else:
            video = video_json["items"][0]

        video_data = {
            "title": video["snippet"]["title"],
            "url": video_url,
            "preview_url": video["snippet"]["thumbnails"]["standard"]["url"],
            "date_published": video["snippet"]["publishedAt"].split("T")[0],
            "source": "YouTube",
            "channel": video["snippet"]["channelTitle"],
            "duration": video["contentDetails"]["duration"].split("T")[1],
            "archived": False,
            "free_to_reuse": video["contentDetails"]["licensedContent"],
            "authorized_to_reuse": video["contentDetails"]["licensedContent"],
        }

        validation_result = validate_video_creation_data(video_data)

        if validation_result is not None:
            return validation_result
        url = video_data["url"]
        existing_video = VideoDAO.find_video_by_url(url)

        if existing_video:
            video_data["date_published"] = datetime.strptime(
                video_data["date_published"], "%Y-%m-%d"
            )
            existing_video.update(video_data)
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

        response["video"] = map_to_dto(video)
        return response, 200


@video_ns.route("/<int:id>/sections")
class VideoSections(Resource):
    @token_required
    @video_ns.expect(add_video_sections)
    @video_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def post(self, id):
        video = VideoDAO.find_video_by_id(id)
        if not video:
            return RESOURCE_NOT_FOUND, 404
        data = request.json
        validation_result = validate_video_sections_data(data)
        if validation_result:
            return validation_result, 400
        section_ids = data["sections"]
        sections = SectionDAO.find_sections_by_ids(section_ids)
        note = ""
        if sections.count() != len(section_ids):
            note = "Not all sections are valid/existing!"
        all_sections_added = VideoDAO.add_video_sections(video, sections)
        if not all_sections_added:
            note += " Duplicate video sections detected and they were not added!"
        response = {"message": "Video sections added successfully."}, 201
        if note:
            response = {"message": note}, 201
        return response


@video_ns.route("/stream/<string:videoId>/<int:format>")
class GetVideoStream(Resource):
    def get(self, videoId, format):
        try:
            info = youtube_dl_extract_info(videoId)
        except youtube_dl.utils.DownloadError as e:
            return {"message": e.args[0]}

        stream_info = youtube_dl_extract_format(info, format)

        return {"stream": stream_info}, 200


@video_ns.route('/<int:id>')
class DeleteVideo(Resource):
    @token_required
    @video_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def delete(self, id):
        video = VideoDAO.find_video_by_id(id)
        if not video:
            return RESOURCE_NOT_FOUND, 404

        VideoDAO.delete_video(video)
        return {"message": "Video Deleted Successfully."}, 200
