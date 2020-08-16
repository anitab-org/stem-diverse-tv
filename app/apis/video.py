from flask import request, Response
import json
from flask_restplus import Api, Resource, Namespace
from app.database.models.author import AuthorModel
from app.database.models.videos import VideoModel
from app.database.models.users import UserModel
from app.database.models.section import SectionModel
from app.database.models.category import CategoryModel
from app.database.sqlalchemy_extension import db

api = Namespace('video', description='Video Library')

@api.route('/latest')
class VideoLibrary(Resource):
    def get(self):
        with open('./content/latests.json') as f:
            return json.loads(f.read())
        return jsonify({'message': 'File does not exist.'})
