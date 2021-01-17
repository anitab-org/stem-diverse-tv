from flask import request, Response
import json
from flask_restplus import Api, Resource, Namespace

from app.apis.dao.section_dao import SectionDAO
from app.database.models.category import CategoryModel
from app.apis.models.video import *
from app.apis.validations.video import validate_video_creation_data
from app.apis.dao.video_dao import VideoDAO
from app.apis.dao.author_dao import AuthorDAO
from datetime import datetime
from ..mappers.video_mapper import map_to_dto

video_ns = Namespace('video', description='Video Library')
add_models_to_namespace(video_ns)


@video_ns.route('/add_category')
class AddCategory(Resource):

    @video_ns.doc(params={'title': 'Title of category'})
    def post(self):
        args = request.args
        title = args["title"]
        existing_category = CategoryModel.find_by_title(title)
        if existing_category:
            return {'message': 'Category already exists'}, 409

        ''' Saving title in capitalized letter. Which can prevent inconsistency in finding existing category title. '''
        category = CategoryModel(title.capitalize())
        category.save_to_db()

        return {'message': 'Category added'}, 201


@video_ns.route('/latest')
class VideoLibrary(Resource):
    def get(self):
        with open('./content/latests.json') as f:
            return json.loads(f.read())
        return jsonify({'message': 'File does not exist.'})


@video_ns.route('/')
class Video(Resource):
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
            response["notes"].append("Some of the authors are not valid or they do not exist.")

        # find sections from the list
        sections = SectionDAO.find_sections_by_ids(data["category_sections"])
        if sections.count() != len(data["category_sections"]):
            response["notes"].append("Some of the sections are not valid or they do not exist.")

        # remove association fields
        data.pop("authors")
        data.pop("category_sections")

        if existing_video:
            data["date_published"] = datetime.strptime(data["date_published"], "%Y-%m-%d")
            existing_video.update(data)
            VideoDAO.replace_video_authors(existing_video, authors)
            VideoDAO.replace_video_sections(existing_video, sections)
            video = existing_video
        else:
            video = VideoDAO.create_video(data["title"], data["url"], data["preview_url"],
                                          datetime.strptime(data["date_published"], "%Y-%m-%d"), data["source"],
                                          data["channel"], data["duration"], data.get("archived"),
                                          data.get("free_to_reuse"), data.get("authorized_to_reuse"))
            VideoDAO.add_video_authors(video, authors)
            VideoDAO.add_video_sections(video, sections)

        response["video"] = map_to_dto(video)
        return response, 200
