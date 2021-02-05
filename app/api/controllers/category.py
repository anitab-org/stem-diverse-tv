from flask import request
from flask_restplus import Namespace, Resource

from app.api.models.category import *
from app.database.models.category import CategoryModel
from app.api.middlewares.auth import token_required
from app.utils.messages import RESOURCE_NOT_FOUND
from ..dao.category_dao import CategoryDAO
from ..dao.section_dao import SectionDAO
from ..validations.category import validate_category_sections_data

category_ns = Namespace("categories", description="Category Details")
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


@category_ns.route("/<int:id>/sections")
class CategorySection(Resource):
    @token_required
    @category_ns.expect(add_category_sections)
    @category_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def post(self, id):
        category = CategoryDAO.find_category_by_id(id)
        if not category:
            return RESOURCE_NOT_FOUND, 404
        data = request.json
        validation_result = validate_category_sections_data(data)
        if validation_result:
            return validation_result, 400
        section_ids = data["sections"]
        sections = SectionDAO.find_sections_by_ids(section_ids)
        note = ""
        if sections.count() != len(section_ids):
            note = "Not all sections are valid/existing!"
        all_sections_added = CategoryDAO.add_category_sections(category, sections)
        if not all_sections_added:
            note += " Duplicate category sections detected are they were not added!"
        response = {"message": "Category sections added successfully."}, 201
        if note:
            response = {"message": note}, 201
        return response
