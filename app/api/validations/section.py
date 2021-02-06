def validate_section_data(data):
    if "title" not in data:
        return {"message": "Title of the section must be provided."}, 400
    if "category" not in data:
        return {"message": "Category title must be provided."}, 400


def validate_updatable_section_data(data):
    if "title" not in data:
        return {"message": "Title of the section must be provided."}, 400
    if len(data.keys()) > 1:
        return {
            "message": "Inappropriate data structure. Only title should be provided."
        }, 400
