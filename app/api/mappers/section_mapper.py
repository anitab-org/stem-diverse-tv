"""
Mapping from model object to representation object"
"""
from typing import List


def map_to_dto(section):
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
    }


def map_to_dto_list(sections: List["SectionModel"]):
    """
    :param sections: list of Section objects
    :return: corresponding response list made by mapping objects to DTOs
    {
    id: <section id>
    title: "<section title>",
    }
    """
    section_repr_list = list(map(lambda section: map_to_dto(section), sections))
    return section_repr_list
