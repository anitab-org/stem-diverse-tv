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

@api.route('/add_category')
class AddCategory(Resource):
    
    @api.doc(params={'title': 'Title of category'})
    def post(self):
        args = request.args
        title = args["title"]
        existing_category = CategoryModel.find_by_title(title)
        if existing_category:
            return {'message': 'Category already exists'}, 409
        
        category = CategoryModel(title.capitalize())
        category.save_to_db()
        return {'message': 'Category added'}, 201

@api.route('/latest')
class VideoLibrary(Resource):
    def get(self):
        with open('./content/latests.json') as f:
            return json.loads(f.read())
        return jsonify({'message': 'File does not exist.'})
