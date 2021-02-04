from flask import request
from flask_restplus import Namespace, Resource
from app.database.models.category import CategoryModel
from app.api.models.category import *
from app.api.dao.category_dao import CategoryDAO
from app.api.mappers.category_mapper import map_to_dto
from app.api.middlewares.auth import token_required
from app.utils.messages import (
    RESOURCE_NOT_FOUND,
    CATEGORY_TITLE_NOT_UPDATED,
)

category_ns = Namespace("category", description="Category Details")
add_models_to_namespace(category_ns)


@category_ns.route("/")
class Category(Resource):
    @token_required
    @category_ns.doc(params={"title": "Title of category"})
    @category_ns.doc(
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


@category_ns.route("/all")
class AllCategories(Resource):
    def get(self):
        category_models = CategoryModel.query.all()
        result = list()
        for category in category_models:
            result.append(category.json())
        return {"categories": result}, 200


@category_ns.route("/<int:id>")
class UpdateCategory(Resource):
    @token_required
    @category_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    @category_ns.expect(update_category_model)
    def patch(self, id):
        payload = request.json
        category = CategoryDAO.find_category_by_id(id)

        if "title" not in payload:
            return {"message": "Title of the category must be provided."}, 400

        if not category:
            return RESOURCE_NOT_FOUND, 404

        if payload["title"] == category.title:
            return CATEGORY_TITLE_NOT_UPDATED, 400

        updated_category = CategoryDAO.update_category(category, payload["title"])
        return map_to_dto(updated_category), 200
