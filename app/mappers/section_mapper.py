"""
Mapping from model object to representation object"
"""
def map_to_response(section):
    """
    :param section: Section object
    :return: corresponding response made by mapping object to DTO
    {
    id: <section id>
    title: "<section title>"
    }
    """
    return {
        "id": section.id,
        "title": section.title,
    }, 201
