from app.utils.messages import SECTIONS_NOT_PROVIDED


def validate_category_sections_data(data):
    if "sections" not in data:
        return SECTIONS_NOT_PROVIDED
