from flask import request, Response
import json
from app.utils import messages
from flask_restplus import Api, Resource, Namespace, fields, Model
from app.database.models.author import AuthorModel
from app.apis.models.author import add_author_model
from app.apis.validations.author import validate_author_details
from app.utils.view_decorator import token_required
author_ns = Namespace('author', description='Author Details')
author_ns.models[add_author_model.name] = add_author_model

@author_ns.route('/')
class AddAuthor(Resource):
    
    @author_ns.expect(add_author_model)
    def post(self):
        
        data = request.json
        validate_result = validate_author_details(data)
        
        if validate_result != {}:
            return validate_result, 400
        
        name = data["name"]
        profile_image = data["profile_image"]
        
        existing_author = AuthorModel.find_by_name(name)
        
        if existing_author:
            return messages.AUTHOR_ALREADY_EXISTS, 400
        else:
            author = AuthorModel(name=name, profile_image=profile_image)
            author.save_to_db()
        
        return messages.AUTHOR_ADDED_SUCCESSFULLY, 200
    
    @author_ns.doc(params={'authorization': {'in': 'header', 'description': 'An authorization token'}})
    def get(self):
        authors = AuthorModel.query.all()
        all_authors = list()
        for author in authors:
            all_authors.append(author.json())
        return {"authors": all_authors}, 200
