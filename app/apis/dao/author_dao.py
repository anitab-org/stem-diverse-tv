from app.database.models.author import AuthorModel
from typing import List


class AuthorDAO:
    @staticmethod
    def find_author_by_id(id: int) -> 'AuthorModel':
        """
        Search author by id.
        :param id: id of the author : int
        :return: Author with the given id (or None)
        """
        return AuthorModel.query.get(id)

    @staticmethod
    def find_authors_by_name(name: str) -> List['AuthorModel']:
        """
        Search author by names (if author name contain `name` string)
        :param name: name (or part of it): <str>
        :return: List of AuthorModel object which name contains the given term
        """
        return AuthorModel.query.filter(AuthorModel.name.contains(name))


