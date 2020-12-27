from flask_restplus import Namespace, Resource
from app.apis.models.section import *
from flask import request, Response
from .validations.section import validate_section_data
from .dao.section_dao import SectionDAO
from .dao.category_dao import CategoryDAO
from ..mappers.section_mapper import map_to_response
from ..utils.messages import SECTION_ALREADY_EXISTS
from sqlalchemy.exc import SQLAlchemyError

section_ns = Namespace('section', description='Section Details')
add_models_to_namespace(section_ns)


@section_ns.route('/')
class Section(Resource):
    @section_ns.expect(add_section_model)
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
