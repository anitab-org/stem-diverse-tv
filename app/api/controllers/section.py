from flask_restplus import Namespace, Resource
from flask import request
from sqlalchemy.exc import SQLAlchemyError

from app.api.models.section import *
from app.api.validations.section import validate_section_data
from app.api.dao.section_dao import SectionDAO
from app.api.dao.category_dao import CategoryDAO
from app.api.mappers.section_mapper import map_to_response
from app.utils.messages import SECTION_ALREADY_EXISTS
from app.api.middlewares.auth import token_required

section_ns = Namespace("sections", description="Section Details")
add_models_to_namespace(section_ns)


@section_ns.route("/")
class Section(Resource):
    @token_required
    @section_ns.expect(add_section_model)
    @section_ns.doc(
        params={
            "authorization": {"in": "header", "description": "An authorization token"}
        }
    )
    def post(self):
        data = request.json
        validation_result = validate_section_data(data)
        if validation_result is not None:
            return validation_result
        title, category_title = data["title"], data["category"]
        existing_section = SectionDAO.find_section_by_title(title)
        if existing_section is not None:
            return SECTION_ALREADY_EXISTS, 400
        try:
            section = SectionDAO.create_section(title)
            category = CategoryDAO.create_or_find_category(category_title)
            category.add_category_section(section)
        except SQLAlchemyError as e:
            return {"message": f"Data cannot be persisted. Original error: {e}"}, 500
        return map_to_response(section)
