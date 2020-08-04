from app.utils import messages

def validate_author_details(data):
    if "name" not in data:
        return messages.NAME_IS_MISSING
    return {}
