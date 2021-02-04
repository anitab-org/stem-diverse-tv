"""
Mapping from model object to representation object"
"""


def map_to_dto(category):
    """
    :param category: Category object
    :return: corresponding response made by mapping object to DTO
    {
    id: <category id>
    title: "<category title>"
    }
    """
    return {
        "id": category.id,
        "title": category.title,
    }
