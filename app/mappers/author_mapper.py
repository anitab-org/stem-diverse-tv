"""
Mapping from model object to representation object"
"""
from typing import List

from app.database.models.author import AuthorModel


def map_to_dto(author: 'AuthorModel'):
    """
    :param author: Author object
    :return: corresponding response made by mapping object to DTO
    {
    id: <section id>
    name: "<section title>",
    profile_image: "<image link>"
    }
    """
    return author.json() if author else None


def map_to_dto_list(authors: List['AuthorModel']):
    """
    :param authors: list of Author objects
    :return: corresponding response list made by mapping objects to DTOs
    {
    id: <section id>
    name: "<section title>",
    profile_image: "<image link>"
    }
    """
    author_repr_list = []
    for author in authors:
        author_repr_list.append(map_to_dto(author))
    return author_repr_list

