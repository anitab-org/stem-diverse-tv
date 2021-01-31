from app.database.models.section import SectionModel
from typing import List


class SectionDAO:
    @staticmethod
    def create_section(title: str) -> "SectionModel":
        """
        Create new section if the params fields are valid and section is not created before.
        :param title: "section title",
        :return:
        """
        section = SectionModel(title=title)
        section.save_to_db()
        return section

    @staticmethod
    def find_section_by_title(title: str) -> "SectionModel":
        """
        Find section that has the given title (if any).
        :param title: title of the section
        :return: SectionModel object (or None)
        """
        return SectionModel.query.filter_by(title=title).first()

    @staticmethod
    def find_sections_by_ids(ids: List[int]) -> List["SectionModel"]:
        """
        Search sections by list of ids
        :param ids: list of ids
        :return: List of SectionModel object which ids are provided
        """
        return SectionModel.query.filter(SectionModel.id.in_(ids))
