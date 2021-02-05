from flask import request
from flask_restplus import Namespace, Resource
from app.api.dao.section_dao import SectionDAO
from app.api.dao.category_dao import CategoryDAO
from app.database.models.category import CategoryModel
from app.api.middlewares.auth import token_required
from app.api.mappers.section_mapper import *
from app.utils.messages import RESOURCE_NOT_FOUND

category_ns = Namespace("category", description="Category Details")


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


@category_ns.route("/<int:id>/section")
class CategorySection(Resource):
    @token_required
    @category_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def get(self, id):
        category = CategoryDAO.find_category_by_id(id)
        if not category:
            return RESOURCE_NOT_FOUND, 404
        sections = SectionDAO.find_sections_by_category(category)
        return map_to_dto_list(sections), 200