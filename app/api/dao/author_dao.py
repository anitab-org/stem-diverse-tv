from app.database.models.author import AuthorModel
from app.database.models.video import VideoModel

from typing import List


class AuthorDAO:
    @staticmethod
    def find_author_by_id(id: int) -> "AuthorModel":
        """
        Search author by id.
        :param id: id of the author : int
        :return: Author with the given id (or None)
        """
        return AuthorModel.query.get(id)

    @staticmethod
    def find_authors_by_name(name: str) -> List["AuthorModel"]:
        """
        Search author by names (if author name contain `name` string)
        :param name: name (or part of it): <str>
        :return: List of AuthorModel object which name contains the given term
        """
        return AuthorModel.query.filter(AuthorModel.name.contains(name))

    @staticmethod
    def find_authors_by_ids(ids: List[int]) -> List["AuthorModel"]:
        """
        Search authors by list of ids
        :param ids: list of ids
        :return: List of AuthorModel object which ids are provided
        """
        return AuthorModel.query.filter(AuthorModel.id.in_(ids))

    @staticmethod
    def add_video_to_authors_defined_by_ids(
        author_ids: List[int], video: "VideoModel"
    ) -> None:
        """
        Add video to the video authors relation (for multiple authors)
        :param author_ids: authors list
        :param video: VideoModel object
        :return: None
        """
        authors = AuthorDAO.find_authors_by_ids(author_ids)
        AuthorDAO.add_video_to_authors(authors, video)

    @staticmethod
    def add_video_to_authors(authors: List["AuthorModel"], video: "VideoModel") -> None:
        """
        Add video to the video authors relation (for multiple authors)
        :param authors: authors list
        :param video: VideoModel object
        :return: None
        """
        for author in authors:
            author.add_video(video)

    @staticmethod
    def update_video_authors(authors: List["AuthorModel"], video: "VideoModel") -> None:
        """
        Add video to the video authors relation (for multiple authors)
        :param authors: authors list
        :param video: VideoModel object
        :return: None
        """

        for author in authors:
            author.add_video(video)
