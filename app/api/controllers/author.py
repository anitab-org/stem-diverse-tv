from flask import request
from flask_restplus import Resource, Namespace

from app.api.dao.author_dao import AuthorDAO
from app.api.validations.author import validate_author_details
from app.database.models.author import AuthorModel
from app.api.mappers.author_mapper import map_to_dto, map_to_dto_list
from app.utils import messages
from app.api.middlewares.auth import token_required

author_ns = Namespace("authors", description="Author Details")
add_models_to_namespace(author_ns)


@author_ns.route("/")
class AuthorList(Resource):
    @token_required
    @author_ns.expect(add_author_model)
    @author_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
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

    @token_required
    @author_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def get(self):
        authors = AuthorModel.query.all()
        all_authors = list(map(lambda author: author.json(), authors))
        return {"authors": all_authors}, 200


@author_ns.route("/<int:id>")
class Author(Resource):
    @token_required
    @author_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def get(self, id):
        """
        Returns author with the given id (if any), else null.
        :param id: id of the author
        :return: author representation or null
        """
        author = AuthorDAO.find_author_by_id(id)
        return map_to_dto(author), 200


@author_ns.route("/<string:name>", "/q")
# NOTE: it's better to follow route pattern -> every search endpoint could
# start with this
class AuthorsByName(Resource):
    @token_required
    @author_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def get(self, name=None):
        """
        Returns authors with the given name (if any), else null.
        :param name: name of the author
        :return: list of author representations or empty list
        """
        if name is None:
            name = request.args.get("name")
        authors = AuthorDAO.find_authors_by_name(name)
        return {"authors": map_to_dto_list(authors)}, 200
